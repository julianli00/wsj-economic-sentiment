import pandas as pd
import json
from config import *
import os
import numpy as np
import re

def load_annotated_data():
    """Load annotated data"""
    # 确保目录存在
    os.makedirs(os.path.dirname(ANNOTATED_DATA_FILE), exist_ok=True)
    return pd.read_csv(ANNOTATED_DATA_FILE)

def process_annotations(data):
    """Process annotations, separate values and descriptions"""
    # Split annotations into value and description
    data[['Annotation_1_part1', 'Annotation_1_part2']] = data['Annotation_1'].str.split(r'[: ]', n=1, expand=True)
    data[['Annotation_2_part1', 'Annotation_2_part2']] = data['Annotation_2'].str.split(r'[: ]', n=1, expand=True)
    return data

def calculate_annotation_frequencies(data):
    """Calculate frequencies of annotation values"""
    count_1 = data['Annotation_1_part1'].value_counts()
    count_2 = data['Annotation_2_part1'].value_counts()
    
    print("Frequency of annotations in Annotation_1_part1:")
    print(count_1)
    print("\nFrequency of annotations in Annotation_2_part1:")
    print(count_2)
    
    return count_1, count_2

def calculate_agreement_rate(data):
    """Calculate inter-annotator agreement rate"""
    # Calculate matching rows
    matching_count = (data['Annotation_1_part1'] == data['Annotation_2_part1']).sum()
    
    # Total rows (excluding NaN)
    total_count = data[['Annotation_1_part1', 'Annotation_2_part1']].dropna().shape[0]
    
    # Calculate agreement rate
    agreement_ratio = matching_count / total_count
    print(f"\nAgreement between annotators: {agreement_ratio:.2%}")
    
    return agreement_ratio

def find_disagreements(data):
    """Find cases where annotators disagree"""
    disagreements = data[data['Annotation_1_part1'] != data['Annotation_2_part1']]
    return disagreements

def calculate_average_difference(data):
    """Calculate average difference between annotation values"""
    # Convert to numeric
    data['Annotation_1_part1'] = pd.to_numeric(data['Annotation_1_part1'], errors='coerce')
    data['Annotation_2_part1'] = pd.to_numeric(data['Annotation_2_part1'], errors='coerce')
    
    # Calculate differences
    diff = abs(data['Annotation_1_part1'] - data['Annotation_2_part1'])
    
    # Remove zero differences
    diff_non_zero = diff[diff != 0]
    
    # Calculate average difference
    mean_diff_non_zero = diff_non_zero.mean()
    print(f"\nAverage difference (excluding 0s): {mean_diff_non_zero:.4f}")
    
    return mean_diff_non_zero

def generate_analysis_report(data, frequencies, agreement_rate, avg_difference, disagreements):
    """Generate analysis report"""
    return {
        "annotation_frequencies": {
            "annotation_1": frequencies[0].to_dict(),
            "annotation_2": frequencies[1].to_dict()
        },
        "agreement_rate": float(agreement_rate),
        "average_difference": float(avg_difference),
        "number_of_disagreements": len(disagreements),
        "disagreement_examples": disagreements[["Title", "URL", "Annotation_1", "Annotation_2"]].to_dict('records')
    }

def preprocess_annotations(df):
    """Preprocess annotations by extracting numeric values"""
    # Extract first number from annotation string
    def extract_number(text):
        if pd.isna(text):
            return np.nan
        try:
            # Extract first number (can be negative)
            match = re.search(r'-?\d+', str(text))
            return float(match.group()) if match else np.nan
        except:
            return np.nan
    
    # Extract numeric values
    df['Annotation_1_value'] = df['Annotation_1'].apply(extract_number)
    df['Annotation_2_value'] = df['Annotation_2'].apply(extract_number)
    
    return df

def calculate_agreement(annotated_data, output_file=None):
    """Calculate agreement metrics between annotators"""
    print("Starting agreement analysis...")
    
    # Load annotated data
    df = pd.read_csv(annotated_data)
    
    # Preprocess annotations
    df = preprocess_annotations(df)
    
    # Calculate agreement metrics
    agreement_count = 0
    total_count = 0
    disagreement_count = 0
    total_difference = 0
    difference_count = 0
    disagreements = []
    
    # Calculate frequencies for each annotator
    freq_1 = df['Annotation_1_value'].value_counts().to_dict()
    freq_2 = df['Annotation_2_value'].value_counts().to_dict()
    
    # Calculate agreement for each row
    for _, row in df.iterrows():
        if pd.notna(row['Annotation_1_value']) and pd.notna(row['Annotation_2_value']):
            total_count += 1
            if row['Annotation_1_value'] == row['Annotation_2_value']:
                agreement_count += 1
            else:
                disagreement_count += 1
                # Calculate difference for all disagreements
                total_difference += abs(row['Annotation_1_value'] - row['Annotation_2_value'])
                difference_count += 1
                # Store disagreement case
                disagreements.append({
                    'Title': row['Title'],
                    'Category': row['Category'],
                    'URL': row['URL'],
                    'Annotation_1': row['Annotation_1'],
                    'Annotation_2': row['Annotation_2'],
                    'Difference': abs(row['Annotation_1_value'] - row['Annotation_2_value'])
                })
    
    # Calculate metrics
    agreement_rate = (agreement_count / total_count * 100) if total_count > 0 else 0
    avg_difference = (total_difference / difference_count) if difference_count > 0 else 0
    
    # Create results DataFrame
    results = pd.DataFrame({
        'Metric': ['Agreement Rate', 'Total Rows', 'Agreement Count', 'Disagreement Count', 'Average Difference'],
        'Value': [f"{agreement_rate:.2f}%", total_count, agreement_count, disagreement_count, f"{avg_difference:.4f}"]
    })
    
    # Create detailed report
    report = {
        'agreement_rate': agreement_rate,
        'total_rows': total_count,
        'agreement_count': agreement_count,
        'disagreement_count': disagreement_count,
        'average_difference': avg_difference,
        'annotation_frequencies': {
            'annotator_1': freq_1,
            'annotator_2': freq_2
        },
        'disagreements': disagreements
    }
    
    # Save results
    if output_file is None:
        output_file = os.path.join(ANALYSIS_DIR, 'analysis_report.json')
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    
    print(f"\nAnalysis report saved to: {output_file}")
    
    # Print disagreement cases
    if disagreements:
        print("\nDisagreement Cases:")
        print("-" * 80)
        for i, case in enumerate(disagreements, 1):
            print(f"\nCase {i}:")
            print(f"Title: {case['Title']}")
            print(f"Category: {case['Category']}")
            print(f"Annotation 1: {case['Annotation_1']}")
            print(f"Annotation 2: {case['Annotation_2']}")
            print(f"Difference: {case['Difference']}")
            print(f"URL: {case['URL']}")
            print("-" * 80)
    
    return results

def main():
    """Main function to run agreement analysis"""
    results = calculate_agreement(ANNOTATED_DATA_FILE)
    print("\nAgreement Analysis Results:")
    print(results.to_string(index=False))

if __name__ == "__main__":
    main() 
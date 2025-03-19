import pandas as pd
import numpy as np
import os
import glob
from config import (
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    READY_FOR_ANNOTATION_FILE,
    ANNOTATORS,
    RANDOM_SEED
)

def load_raw_data():
    """Load raw data from the first CSV file in raw directory"""
    # Get all CSV files in raw directory
    csv_files = glob.glob(os.path.join(RAW_DATA_DIR, "wsj_US_econ_articles_*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {RAW_DATA_DIR}")
    
    # Sort by filename and get the first file
    first_file = sorted(csv_files)[0]
    print(f"Loading data from: {first_file}")
    
    return pd.read_csv(first_file)

def assign_annotators(df):
    """Assign annotators to data following the notebook logic"""
    # Initialize assignment count for each person
    assignments_count = {person: 0 for person in ANNOTATORS}
    assigned_people_list = []
    
    # Iterate through each row for assignment
    for _ in range(len(df)):
        # Sort people by their assignment count, with special weight for Yiwen Chen
        sorted_people = sorted(
            ANNOTATORS,
            key=lambda person: assignments_count[person] if person != 'Yiwen Chen' else assignments_count[person] / 1.7
        )
        
        # Assign to the two people with least assignments
        assigned_people = [sorted_people[0], sorted_people[1]]
        assigned_people_list.append(assigned_people)
        
        # Update counts
        assignments_count[assigned_people[0]] += 1
        assignments_count[assigned_people[1]] += 1
    
    # Add annotator columns
    df['Annotation_1'] = [assigned[0] for assigned in assigned_people_list]
    df['Annotation_2'] = [assigned[1] for assigned in assigned_people_list]
    
    # Print assignment statistics
    for person, count in assignments_count.items():
        print(f'{person} is assigned {count} rows.')
    
    return df

def preprocess_data(sample_size=200):
    """Preprocess raw data and assign to annotators"""
    print(f"Starting data preprocessing, sample size: {sample_size}...")
    
    # Load raw data
    df = load_raw_data()
    
    # Sample data if needed
    if sample_size and len(df) > sample_size:
        # Set random seed for reproducibility
        np.random.seed(RANDOM_SEED)
        df = df.sample(n=sample_size)
    
    # Assign annotators
    df = assign_annotators(df)
    
    # Save processed data
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
    df.to_csv(READY_FOR_ANNOTATION_FILE, index=False)
    print(f"Data saved to {READY_FOR_ANNOTATION_FILE}")
    
    return df

def select_data_for_annotation(raw_data, n_samples=200):
    """Select data for annotation"""
    return raw_data[["Date", "Title", "Category", "URL"]].sort_values(
        by="Date", ascending=False
    ).head(n_samples).reset_index(drop=True)

def main(n_samples=200, output_file=None):
    """Main function
    
    Args:
        n_samples (int): Number of samples to select
        output_file (str, optional): Output file path, use default if None
    """
    # Load raw data
    raw_data = load_raw_data()
    
    # Select data for annotation
    selected_data = select_data_for_annotation(raw_data, n_samples)
    
    # Assign annotators
    annotated_data = assign_annotators(selected_data)
    
    # Determine output path
    output_path = output_file if output_file else READY_FOR_ANNOTATION_FILE
    
    # Save results
    annotated_data.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    main() 
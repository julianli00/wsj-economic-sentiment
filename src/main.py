import argparse
import os
from scraper import scrape_wsj_archive
from data_preprocessing import preprocess_data
from agreement_analysis import calculate_agreement
from config import (
    PROCESSED_DATA_DIR,
    ANNOTATED_DATA_FILE,
    ANALYSIS_DIR,
    ANALYSIS_REPORT_FILE,
    RAW_DATA_DIR,
    ANNOTATED_DATA_DIR
)

def main():
    """Main function to handle different modes of operation"""
    parser = argparse.ArgumentParser(description='WSJ Article Scraping and Annotation Tool')
    parser.add_argument('--mode', choices=['scrape', 'preprocess', 'analyze'], required=True,
                      help='Operation mode: scrape, preprocess, or analyze')
    
    # Arguments for scrape mode
    parser.add_argument('--start-date', help='Start date for scraping (YYYY-MM-DD)')
    parser.add_argument('--end-date', help='End date for scraping (YYYY-MM-DD)')
    
    # Arguments for preprocess mode
    parser.add_argument('--samples', type=int, default=200,
                      help='Number of samples to select (default: 200)')
    
    # Arguments for analyze mode
    parser.add_argument('--output', help='Output file path for analysis results')
    
    args = parser.parse_args()
    
    # Create all necessary directories
    for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, ANNOTATED_DATA_DIR, ANALYSIS_DIR]:
        os.makedirs(directory, exist_ok=True)
    
    # Handle different modes
    if args.mode == 'scrape':
        if not args.start_date or not args.end_date:
            parser.error("Scrape mode requires --start-date and --end-date")
        scrape_wsj_archive(args.start_date, args.end_date)
        
    elif args.mode == 'preprocess':
        preprocess_data(args.samples)
        
    elif args.mode == 'analyze':
        output_file = args.output if args.output else ANALYSIS_REPORT_FILE
        if not os.path.dirname(output_file):
            output_file = os.path.join(ANALYSIS_DIR, output_file)
        results = calculate_agreement(ANNOTATED_DATA_FILE, output_file)
        print("\nAgreement Analysis Results:")
        print(results.to_string(index=False))

if __name__ == "__main__":
    main()

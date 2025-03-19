import argparse

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='WSJ News Sentiment Annotation Tool')
    
    parser.add_argument(
        '--mode', 
        type=str, 
        choices=['scrape', 'preprocess', 'analyze'],
        required=True,
        help='Select mode: scrape(collect data), preprocess(data preprocessing), or analyze(agreement analysis)'
    )
    
    # Scraper parameters
    parser.add_argument(
        '--start-date',
        type=str,
        help='Start date for scraping (YYYY-MM-DD format)'
    )
    
    parser.add_argument(
        '--end-date',
        type=str,
        help='End date for scraping (YYYY-MM-DD format)'
    )
    
    # Preprocessing parameters
    parser.add_argument(
        '--samples',
        type=int,
        default=200,
        help='Number of samples for preprocessing (default: 200)'
    )
    
    # Common parameters
    parser.add_argument(
        '--output',
        type=str,
        help='Output file path (optional)'
    )
    
    return parser.parse_args() 
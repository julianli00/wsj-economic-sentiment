import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import os
import time
from tqdm import tqdm

# Headers for requests
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

def fetch_page(url, retries=3):
    """Fetch a page with retry mechanism"""
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.status_code == 200:
                return response
            print(f"Attempt {attempt + 1}: Failed to fetch {url}, status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1}: Request error - {e}")
        
        if attempt < retries - 1:
            delay = 2 ** attempt
            print(f"Waiting {delay} seconds before next attempt...")
            time.sleep(delay)
    return None

def parse_article_data(soup, date_str):
    """Parse article data from BeautifulSoup object"""
    articles = []
    article_links = soup.select(".WSJTheme--headline--unZqjb45 a")
    categories = soup.select(".WSJTheme--articleType--34Gt-vdG")
    
    for i in range(len(article_links)):
        title = article_links[i].get_text(strip=True)
        article_url = article_links[i]["href"] if "href" in article_links[i].attrs else "Unknown"
        category = categories[i].get_text(strip=True) if i < len(categories) else "Unknown"
        
        if category in ["U.S. Economy", "U.S. Markets"]:
            articles.append({
                'Date': date_str,
                'Title': title,
                'Category': category,
                'URL': article_url
            })
    
    return articles

def scrape_date(date_str):
    """Scrape articles for a specific date"""
    articles = []
    page = 1
    max_pages = 1  # Initialize max pages
    
    # First get the maximum number of pages
    url = f"https://www.wsj.com/news/archive/{date_str}?page=1"
    response = fetch_page(url)
    if response:
        soup = BeautifulSoup(response.text, "html.parser")
        pagination = soup.select(".WSJTheme--pagination--1jWoU_y9 a")
        if pagination:
            try:
                max_pages = max(int(a.get_text()) for a in pagination if a.get_text().isdigit())
            except ValueError:
                max_pages = 1
    
    # Create progress bar for page scraping
    with tqdm(total=max_pages, desc=f"Day: {date_str}", 
             bar_format='{desc} | Page: {n_fmt}/{total_fmt} [{bar}] {percentage:3.0f}%',
             leave=False) as pbar:
        while True:
            url = f"https://www.wsj.com/news/archive/{date_str}?page={page}"
            
            response = fetch_page(url)
            if not response:
                break
            
            soup = BeautifulSoup(response.text, "html.parser")
            article_links = soup.select(".WSJTheme--headline--unZqjb45 a")
            
            if not article_links:
                break
            
            new_articles = parse_article_data(soup, date_str)
            articles.extend(new_articles)
            
            # Update progress bar description
            total_titles = len(article_links)
            saved_titles = len(new_articles)
            pbar.set_description(f"Day: {date_str} | Found: {saved_titles}/{total_titles} articles")
            
            page += 1
            pbar.update(1)
            time.sleep(2)  # Random delay between pages
    
    return articles

def main():
    """Main test function"""
    # Set test dates (10 days)
    start_date = datetime(2025, 2, 1)
    all_articles = []
    
    # Create output directory
    os.makedirs("tests/data", exist_ok=True)
    
    # Calculate total days for progress bar
    total_days = 10
    
    # Create progress bar for overall progress
    with tqdm(total=total_days, desc="Total Progress", 
             bar_format='{desc}: {n_fmt}/{total_fmt} Days [{bar}] {percentage:3.0f}%') as pbar:
        for i in range(total_days):
            current_date = start_date + timedelta(days=i)
            date_str = current_date.strftime('%Y/%m/%d')
            
            articles = scrape_date(date_str)
            all_articles.extend(articles)
            pbar.update(1)
    
    # Convert to DataFrame and save
    if all_articles:
        df = pd.DataFrame(all_articles)
        df['id'] = range(1, len(df) + 1)  # Add id column
        output_file = "tests/data/wsj_test_articles.csv"
        df.to_csv(output_file, index=False)
        print(f"\nTest completed! Data saved to {output_file}")
        print(f"Total articles collected: {len(df)}")
    else:
        print("Warning: No articles were collected!")

if __name__ == "__main__":
    main() 
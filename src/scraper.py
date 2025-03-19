import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta
import os
from config import RAW_DATA_DIR
from tqdm import tqdm

# Headers for requests
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

def fetch_page(url, retries=5):
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
    """Parse article data from BeautifulSoup object
    
    Args:
        soup: BeautifulSoup object
        date_str: Date string in YYYY/MM/DD format
    """
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

def scrape_date(date_str, page=1):
    """Scrape articles for a specific date"""
    articles = []
    failed_urls = []
    max_pages = 1  # 初始化最大页数
    
    # 首先获取最大页数
    url = f"https://www.wsj.com/news/archive/{date_str}?page=1"
    response = fetch_page(url)
    if response:
        soup = BeautifulSoup(response.text, "html.parser")
        # 获取分页信息
        pagination = soup.select(".WSJTheme--pagination--1jWoU_y9 a")
        if pagination:
            try:
                max_pages = max(int(a.get_text()) for a in pagination if a.get_text().isdigit())
            except ValueError:
                max_pages = 1
    
    # 使用tqdm创建页面爬取的进度条，设置自定义格式
    with tqdm(total=max_pages, desc=f"Day: {date_str}", 
             bar_format='{desc} | Page: {n_fmt} [{bar}] {percentage:3.0f}%',
             leave=False) as pbar:  # 添加leave=False参数
        while True:
            url = f"https://www.wsj.com/news/archive/{date_str}?page={page}"
            
            response = fetch_page(url)
            if not response:
                failed_urls.append(url)
                break
            
            soup = BeautifulSoup(response.text, "html.parser")
            article_links = soup.select(".WSJTheme--headline--unZqjb45 a")
            
            if not article_links:
                break
            
            new_articles = parse_article_data(soup, date_str)
            articles.extend(new_articles)
            
            # 更新进度条描述，显示当前页面的文章数量
            total_titles = len(article_links)
            saved_titles = len(new_articles)
            pbar.set_description(f"Day: {date_str} | Found: {saved_titles}/{total_titles} articles")
            
            page += 1
            pbar.update(1)  # 更新进度条
            time.sleep(2)  # Random delay between pages
    
    return articles, failed_urls

def scrape_wsj_archive(start_date, end_date):
    """Scrape WSJ article archive
    
    Args:
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format
        
    Returns:
        pd.DataFrame: DataFrame containing scraped article data with columns:
            - Date: Article publication date
            - Title: Article title
            - Category: Article category
            - URL: Article URL
            
    Note:
        Data is saved to data/raw/wsj_US_econ_articles_{start_date}_{end_date}.csv
        Only articles with categories "U.S. Economy" and "U.S. Markets" are saved
    """
    all_articles = []
    all_failed_urls = []
    
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
    
    # 计算总天数用于进度条
    total_days = (end_date_obj - current_date).days + 1
    
    # 使用tqdm创建进度条，设置自定义格式
    with tqdm(total=total_days, desc="Total Progress", bar_format='{desc}: {n_fmt}/{total_fmt} Days [{bar}] {percentage:3.0f}%') as pbar:
        while current_date <= end_date_obj:
            formatted_date = current_date.strftime('%Y/%m/%d')
            articles, failed_urls = scrape_date(formatted_date)
            all_articles.extend(articles)
            all_failed_urls.extend(failed_urls)
            current_date += timedelta(days=1)
            pbar.update(1)  # 更新进度条
    
    if not all_articles:
        print("Warning: No articles were collected!")
        return None
    
    # Convert to DataFrame and save
    df = pd.DataFrame(all_articles)
    
    # Create output file path with both start and end dates
    start_date_str = datetime.strptime(start_date, '%Y-%m-%d').strftime('%Y%m%d')
    end_date_str = datetime.strptime(end_date, '%Y-%m-%d').strftime('%Y%m%d')
    output_file = os.path.join(RAW_DATA_DIR, f'wsj_US_econ_articles_{start_date_str}_{end_date_str}.csv')
    
    # Create directories if they don't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"\nData saved to {output_file}")
    print(f"Total articles collected: {len(df)}")
    
    # Report failed URLs
    if all_failed_urls:
        print("\nThe following URLs failed after 5 attempts:")
        for url in all_failed_urls:
            print(url)
    else:
        print("\nAll URLs were successfully scraped.")
    
    return df

def main(start_date=None, end_date=None):
    """Main function for scraping WSJ articles
    
    Args:
        start_date (str, optional): Start date in 'YYYY-MM-DD' format
        end_date (str, optional): End date in 'YYYY-MM-DD' format
    """
    if not start_date:
        start_date = '2024-01-01'
    if not end_date:
        end_date = '2025-02-26'
    
    print(f"Starting scraping from {start_date} to {end_date}...")
    df = scrape_wsj_archive(start_date, end_date)
    
    if df is not None:
        print("Scraping completed successfully.")
    else:
        print("Scraping failed to collect any articles.")

if __name__ == "__main__":
    main() 
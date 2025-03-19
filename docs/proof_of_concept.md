# Proof of Concept (PoC)

## Overview

This PoC demonstrates a web scraping workflow to extract all articles from The Wall Street Journal (WSJ) archive, analyze their relevance using NLP, and classify them into predefined categories. We then compute similarity scores for each article against the categories "Economy", "Finance", "Business", and "Market". Only articles with a maximum similarity score above 0.75 are included in the output.

## Setup

1. Activate the conda environment:
   ```sh
   conda activate environment.yaml
   ```
2. Install the required spaCy model:
   ```sh
   python -m spacy download en_core_web_md
   ```

## Execution

Run the script:

```sh
python wsj_scraper_test.py
```

## Output

Example output of the script:

```
[ECONOMIC] Australia Could Acquire Country’s Third Largest Airline (Business) - Score: 1.00
[ECONOMIC] Super Micro Computer Stock Climbs on Lofty 2026 Outlook (Business) - Score: 1.00
[ECONOMIC] Lyft Sees Growth Slowdown in Gross Bookings (Business) - Score: 1.00
[ECONOMIC] The WSJ Dollar Index Falls 0.2% to 101.99 (Foreign Exchange) - Score: 0.87
[ECONOMIC] Elon Musk’s Government Efficiency Siege (Future View) - Score: 0.79
[ECONOMIC] Avis Budget CEO Joe Ferraro to Step Down, Brian Choi Named Successor (Business) - Score: 1.00
[ECONOMIC] DOGE Is Elon Musk’s Useful Experiment (Business World) - Score: 0.80
[ECONOMIC] Stay on Top of the Markets With These WSJ Newsletters (Markets) - Score: 1.00
[ECONOMIC] Live Q&A: Our Economics Reporter Answered Your Questions (Economy) - Score: 1.00
[ECONOMIC] Tax Season 2025: What’s New That Could Save You Money (Personal Finance) - Score: 1.00
[ECONOMIC] Powell Says Fed Doesn’t Need to Rush on Rate Cuts (U.S. Economy) - Score: 0.83
```

## Notes

- The script retries failed requests using an exponential backoff strategy.
- It categorizes articles using NLP similarity scores against predefined economic keywords.
- Only articles with a maximum similarity score above 0.75 are classified as economic-related.
- In the next phase, the scraper will collect all WSJ articles from 2023 to 2024 and store them in CSV format.
- The output CSV will contain the following columns:
  ```
  Date, Page, Title, Category, Economy_Score, Finance_Score, Business_Score, Market_Score
  ```


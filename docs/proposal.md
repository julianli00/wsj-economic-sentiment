# Project Proposal

We aim to annotate economic-related articles from The Wall Street Journal to determine whether they express a positive, negative, or neutral sentiment toward the title. We believe this sentiment may carry insights relevant to stock movements. In the future, this analysis could be used as a key method for predicting whether stock prices will rise or fall.

The source of the data is from [Wall Street Journal Archive](https://www.wsj.com/news/archive), the archive of Wall Street Journal.  

The text is the articles. The language is English. The genre is news. The texts are about stocks. The writers from Wall Street Journal wrote them. Each title varies in length, from several words to dozens of words. We want to collect at least 1000 titles for our dataset.  

Yes, we will be targeting the stocks topic. We need to filter the stocks-related articles from all other topics in the Wall Street Journal. We use a simple Python script to do so. There is enough data since we have all the archive articles for over 20 years. We believe we can have more than 2000 data points available, each containing more than 500 words, leading to a total of over 1 million words, which is sufficient for this project.  

The structure consists of article titles. There is metadata about author names and the publication time of the articles, but we are not going to annotate them.  

We will annotate each article based on whether it presents positive, negative, or neutral information about the stock mentioned. The annotation categories will be:
- **Positive**
- **Negative**
- **Neutral**  

We will store all the data, including annotations, in `.csv` files.  

After annotation, this dataset can be used to study the trends of actual stocks in relation to the stock-related articles published at that time. However, to do so, additional information about real stock prices is needed, such as S&P 500 data. We believe this is easy to obtain, as historical stock prices can be downloaded online. Since our dataset already includes the publication date of the articles, it will be straightforward to merge our data with historical stock data.  

Thus, this dataset could be useful for developing a model that predicts future stock trends based on current articles, which could serve as a reference for market traders.

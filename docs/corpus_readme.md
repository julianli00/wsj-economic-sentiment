source of corpus:https://www.wsj.com/news/archive/years.  From wsj archive.

Location where we store the data:

[https://github.ubc.ca/yyyuchen/wsj-corpus-annotation](https://github.ubc.ca/yyyuchen/wsj-corpus-annotation/blob/main/data/wsj_US_econ_articles_2024-01-01_2025-02-26.csv)

The format of storage of data is in csv.

**The length of the corpus:**
There are 391 rows, meaning 391 titles and articles url in total, about the US market.

**The total numbers of tokens:**

Excluding articles, there are 6110 tokens in total. However, if you count the articles, it will be around 100 times of it.

**Known issues:**

There is noise. This is because we want to annotate about the stocks, but there are articles in our dataset that is not about the stocks. We will clean up them manully when annotating.

# Annotated Data Visualization App

## Overview

Web Link: https://huggingface.co/spaces/alexdu271/streamlit_web_annotation_data

A **Streamlit-based web application** for visualizing annotated data. Features:
- **Search across all columns**
- **Paginated data browsing**
- **Interactive annotation visualizations**
- **Deployable on Hugging Face Spaces**

## Files
### `app.py` (Main Application Script)
This file contains the **Streamlit app logic**, including:
- **Data loading** from `annotated_data.csv`
- **Search functionality** (searches across all columns)
- **Pagination** for browsing data
- **Visualization** of annotation distributions and agreement rates

### `annotated_data.csv` (Dataset)
This is the **input dataset** containing annotated text data. The expected columns are:
- `ID` → Unique identifier for each entry.
- `Date` → Date of the news or event.
- `Title` → The title of the news article or event.
- `Category` → The category of the article (e.g., Economy, Markets, etc.).
- `URL` → A link to the original article.
- `Annotation_1` → First annotation (`1` = Positive, `0` = Neutral, `-1` = Negative).
- `Annotation_2` → Second annotation (same values as `Annotation_1`).

## Installation
To run this application locally, install the required dependencies:
```bash
pip install streamlit pandas matplotlib plotly
```

## Run Locally
```bash
streamlit run app.py
```
Access at `http://localhost:8501`.

## Features
### **1. Data Browser**
- **Search any column**
- **Paginated results (10 per page)**

### **2. Data Visualization**
- **Annotation Distribution** (bar chart)
- **Annotation Agreement Rate** (pie chart)

## Code Breakdown
### **1. Data Loading**
- Reads `annotated_data.csv` into a Pandas DataFrame.
- **Cleans `Annotation_1` and `Annotation_2` columns** to ensure only `1`, `0`, and `-1` are included.
- **Prints column names and a data preview** for debugging.

### **2. Search Function**
- Searches for a user-provided **keyword across all columns**.
- Displays **filtered results in a paginated format**.

### **3. Visualization**
- Uses **Plotly** to generate:
  - A **bar chart** for annotation distribution.
  - A **pie chart** for annotation agreement rate.

## Deployment on Hugging Face Spaces
### **1. Create a Space**
- Go to [Hugging Face Spaces](https://huggingface.co/spaces) and create a new space.
- Set **SDK** to `Streamlit`.

### **2. Upload Files**
Upload `app.py` and `annotated_data.csv` directly via the web interface.

**OR** use Git:
```bash
git clone https://huggingface.co/spaces/your-username/your-space
cd your-space
cp /path/to/app.py .
cp /path/to/annotated_data.csv .
git add .
git commit -m "Add Streamlit app"
git push
```

### **3. Add `requirements.txt`**
Create a file named `requirements.txt` in your Hugging Face Space and add:
```txt
streamlit
pandas
matplotlib
plotly
```

### **4. Deploy**
- Click **Deploy** in your Hugging Face Space.
- Wait a few minutes for the app to start running.
- A **public URL** will be generated, where you can access your app.

## Usage
1. **Search** for a keyword to filter data.
2. **Browse** results with pagination.
3. **Visualize** annotation trends.

## Conclusion
This application provides an **interactive way to explore annotated financial/news datasets**. It can be **used for sentiment analysis validation, quality control, or research purposes**.


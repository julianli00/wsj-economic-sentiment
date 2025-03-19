import streamlit as st  # Import Streamlit
import pandas as pd
import plotly.express as px
import re
import os

# Set data file path
ANNOTATED_DATA_FILE = os.path.join('data', 'annotated', 'annotated_data.csv')

# Set page configuration
st.set_page_config(page_title="WSJ Article Annotation Visualization", layout="wide")

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(ANNOTATED_DATA_FILE)
        
        # Display column names to ensure correct parsing
        st.write("📌 Loaded Columns:", df.columns.tolist())
        
        # Show first 5 rows for preview
        st.write("📌 Data Preview:", df.head())
        
        # Rename columns for consistency
        expected_columns = {
            "Annotation_1": "annotation_1",
            "Annotation_2": "annotation_2",
        }
        df = df.rename(columns=expected_columns)
        
        # Ensure annotation columns only contain -1, 0, 1
        def clean_annotation(value):
            if pd.isna(value):
                return 0  # Handle missing values
            match = re.search(r'(-1|0|1)', str(value))  # Extract -1, 0, or 1
            return int(match.group()) if match else 0  # Default to 0 if no match
        
        # Process annotation columns
        if "annotation_1" in df.columns and "annotation_2" in df.columns:
            df["annotation_1"] = df["annotation_1"].apply(clean_annotation)
            df["annotation_2"] = df["annotation_2"].apply(clean_annotation)
        else:
            st.error("❌ `annotation_1` or `annotation_2` column not found. Please check the dataset format!")
            
        return df
    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
        return None

# Main program
def main():
    data = load_data()
    if data is None:
        return

    # Sidebar menu
    menu = st.sidebar.radio("Select Page", ["Data Browser", "Data Visualization"])

    if menu == "Data Browser":
        display_data_browser(data)
    elif menu == "Data Visualization":
        display_data_visualization(data)

def display_data_browser(data):
    st.title("🔍 Annotation Data Browser")
    
    # Search functionality (searches the entire table)
    search_query = st.text_input("🔎 Search (across all columns)", "")
    
    if search_query:
        search_query = search_query.lower()
        mask = data.apply(lambda col: col.astype(str).str.lower().str.contains(search_query, na=False))
        filtered_data = data[mask.any(axis=1)]
    else:
        filtered_data = data
    
    # Pagination
    page_size = 10
    total_pages = (len(filtered_data) // page_size) + 1
    page = st.number_input("Page", min_value=1, max_value=total_pages, step=1, value=1)
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    
    st.dataframe(filtered_data.iloc[start_idx:end_idx])

def display_data_visualization(data):
    st.title("📊 Data Visualization")
    
    if "annotation_1" in data.columns and "annotation_2" in data.columns:
        # Compute annotation distribution
        annotation_counts = data[["annotation_1", "annotation_2"]].apply(pd.Series.value_counts).fillna(0)
        annotation_counts = annotation_counts.astype(int)
        
        st.subheader("🔹 Annotation Distribution")
        fig = px.bar(annotation_counts, barmode="group", 
                    title="Annotation Statistics", 
                    labels={"index": "Annotation Category", "value": "Count"})
        st.plotly_chart(fig)
        
        # Compute annotation agreement
        data["agreement"] = (data["annotation_1"] == data["annotation_2"]).astype(int)
        agreement_rate = data["agreement"].mean()
        
        st.subheader("🔹 Annotation Agreement")
        st.write(f"**Annotator Agreement Rate:** {agreement_rate:.2%}")
        fig_pie = px.pie(names=["Agreement", "Disagreement"], 
                        values=[agreement_rate, 1 - agreement_rate], 
                        title="Annotation Agreement Ratio")
        st.plotly_chart(fig_pie)
    else:
        st.error("❌ `annotation_1` or `annotation_2` column not found. Please check the dataset format!")
    
    # Display sample data
    st.subheader("🔹 Sample Data")
    st.dataframe(data.sample(10))

if __name__ == "__main__":
    main()

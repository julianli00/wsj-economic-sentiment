# **Web Interface Plan: WSJ Stock Sentiment Analysis**

## **1. Goal**  
Build an interactive web interface where users can **search WSJ news headlines**, see their **sentiment labels (positive/negative/neutral)**, and click links to **read full articles**. The backend will use **FastAPI**.

## **2. Main Features**  
### **🔍 Search**  
- Users enter keywords to find WSJ headlines.  
- Results show **headline, sentiment, and article link**.  
- Uses **Whoosh/Elasticsearch** for fast searching.  

### **📊 Filter by Sentiment**  
- Users can **filter** results by sentiment (positive, negative, or neutral).  

### **🔗 View Full Articles**  
- Each result includes a **link** to the full article.  

## **3. Why This Design?**  
- **Simple and easy to use** for quick searches.  
- **Fast and efficient** with indexed search.  
- **Expandable** – future updates can include **sentiment trends** and **charts**.  

## **4. Development Plan**  
- **Backend (FastAPI + Whoosh/Elasticsearch)**: Create API routes `/search` and `/filter`.  
- **Frontend (HTML + JavaScript + Tailwind)**: Design the search page and filters.  
- **Integration**: Test API to ensure smooth data flow.  

## **5. Conclusion**  
This web interface will provide a **fast and interactive** way to explore WSJ news sentiment, helping users find relevant articles easily while allowing future improvements.

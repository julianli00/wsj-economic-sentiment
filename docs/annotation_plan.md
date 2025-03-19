# **U.S. Economic Environment Sentiment Annotation Plan**

## **Annotation Approach**
We will annotate *Wall Street Journal* articles to check if they show **Positive, Negative, or Neutral** sentiment about the **U.S. economic environment**.

### **Dataset Time Range:**
The dataset includes **390 articles** related to the U.S. economy published from **January 1, 2024, to February 26, 2025**.

### **Annotation Rules:**
- **Positive**: The article describes **economic growth, stability, or improvement**, such as strong GDP, low inflation, good job market, or strong financial markets.
- **Negative**: The article talks about **economic decline, crisis, high inflation, rising unemployment, recession risk, or financial instability**.
- **Neutral**: The article presents a **balanced view** or does not clearly express an opinion on the economy.

### **How to Decide:**
- We read the **title** and **main content** to understand the economic sentiment.
- We focus on the **overall U.S. economic environment**, not just individual companies or stocks.

### **Final Label:**
- Every article gets **one label**: **Positive, Negative, or Neutral**.

---

## **Annotation Tools**
- **Manual Annotation**: Each team member will review and label **¼ of the data manually**.
- **Excel**: Created a **new column** on the dataset recording sentiment labels.
- **Python (Pandas, NLTK, Scikit-learn)**:
  - **Data Processing**: Cleaning text, filtering articles related to the economy.
  - **Consistency Check**: Finding annotation errors or inconsistencies.

---

## **Who Will Annotate**
- **Four team members** will divide the work equally (**each annotates ¼ of the data**).

### **Checking Agreement:**
- **25% of the articles will be double-annotated** (two annotators label the same articles).
- This ensures **consistency and accuracy**.

| Annotator        | Unique Articles | Double-Checked Articles |
|-----------------|----------------|------------------------|
| **Yuchen Li**    | 98             | 24                     |
| **Yiyang Du**    | 98             | 24                     |
| **Miaolin Zhang**| 97             | 24                     |
| **Yiwen Chen**   | 97             | 24                     |

---

## **Annotation Schema**
### **Label Options:**
- **Positive (1)** → Economy is improving, strong, or stable.
- **Negative (-1)** → Economy is declining, unstable, or at risk.
- **Neutral (0)** → No strong sentiment or a mix of positive and negative points.

### **How to Label:**
1. Read **title** and **content**.
2. Determine the **overall sentiment** towards the **U.S. economic environment**.
3. Record the label by **adding a new column** on the dataset sheet.

---

## **Expected Annotation Work**
- **Dataset Size**: **390 unique articles** from **January 1, 2024, to February 26, 2025**.
- **Deadline**: **1 week**
- **Goal**: Annotate **all 390 articles**.

### **Time Calculation:**
- If one article takes **5 minutes**, each annotator can do **12 per hour**.
- Each person needs about **8 hours** to finish their part.

---

## **How to Ensure Annotation Quality**
### **Training:**
- We reviewed **example articles** and discussed **difficult cases together**.
- We created a **guideline document** for consistency.

### **Checking Agreement:**
- If **agreement is too low**, we will review **disagreements** and improve the guidelines.

### **Review Process:**
- We will **randomly check a small set of annotations** every week.
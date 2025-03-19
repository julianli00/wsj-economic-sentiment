# WSJ Sentiment Annotation Guidelines

## **1. Task Description**
This annotation task requires annotators to classify **Wall Street Journal (WSJ) articles** as either **Positive** or **Negative** based on the sentiment conveyed in the text.

---

## **2. Annotation Labels**
Annotators should assign one of the following labels:

| Label | Description | Example |
|--------|------------|---------|
| **Positive** | The article expresses optimism, growth, success, or positive economic/financial trends. | "The stock market surged today, closing at an all-time high." |
| **Negative** | The article describes decline, crisis, financial loss, or pessimistic trends. | "Unemployment rates increased sharply as the economy slowed." |

🔹 **Special Cases:**
- If the sentiment is **neutral or unclear**, choose the label that best reflects the overall tone.
- If an article contains **mixed sentiments**, focus on **the dominant sentiment**.

---

## **3. Annotation Instructions**
1. **Read** the article snippet carefully.
2. **Identify the overall sentiment** (Positive or Negative).
3. **If uncertain**, choose the label that best fits the dominant sentiment.

---

## **4. Examples**
### **Example 1**
**Text:** *"The GDP grew by 3% this quarter, signaling a strong economic recovery."*  
✅ **Correct Label:** `Positive`

### **Example 2**
**Text:** *"The Federal Reserve warns of an impending recession."*  
✅ **Correct Label:** `Negative`

### **Example 3**
**Text:** *"Inflation rates continue to rise, causing consumer concerns."*  
✅ **Correct Label:** `Negative`

---

## **5. Mechanical Turk Instructions**
If using **Amazon Mechanical Turk (MTurk)**:
- This guideline should be included in the **task description**.
- The annotation interface should have a **dropdown** with the options: **Positive, Negative**.

---
📌 **For access to the dataset and examples:**  
[GitHub Repo - WSJ Corpus](https://github.ubc.ca/yyyuchen/wsj-corpus-annotation)

# Label Encoding with Pandas and Scikit-learn

This is a simple data preprocessing project that demonstrates how to perform **label encoding** on categorical data using `pandas` and `scikit-learn`.

### 🔧 Technologies Used:
- Python
- Pandas
- scikit-learn

### 📂 Dataset:
The project uses a sample Excel file named `Simple data.xlsx`, which includes columns like:
- `gender` (e.g., Male, Female)
- `passed` (e.g., Yes, No)

### 🧠 What is Label Encoding?
Label Encoding converts **categorical variables** (text labels) into **numeric form** so that machine learning algorithms can use them.

### ✅ Process:
1. Load Excel data using `pandas.read_excel()`
2. Make a copy of the DataFrame
3. Use `LabelEncoder` from `sklearn.preprocessing` to encode:
   - `gender` → `Gender_Encoded`
   - `passed` → `Pass_Encoded`

### 💻 How to Run:

Make sure you have the required libraries installed:

```bash
pip install pandas scikit-learn openpyxl

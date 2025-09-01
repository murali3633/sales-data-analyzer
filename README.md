

# Sales Data Analyzer – Python Project

A Python project that analyzes sales data to provide insights on top products, total revenue, and monthly sales trends using **Pandas** and **Matplotlib**.

---

## 🛠️ Tools Used
- Python 3.x
- Pandas
- Matplotlib
- Jupyter Notebook (optional)

---

## 📂 Dataset
- The project requires only **`sales_data.csv`** as input.
- Dataset contains columns like `Order Date`, `Product Name`, `Quantity`, `Sales`, `Discount`, `Profit`, etc.
- You can download the dataset from [Kaggle Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final).

---

## 🚀 Features
1. Loads and previews the sales dataset.
2. Calculates total revenue from the `Sales` column.
3. Identifies **Top 5 Products by Revenue**.
4. Analyzes **monthly revenue trends**.
5. Generates visualizations:
   - Bar chart for top products.
   - Line chart for monthly revenue trends.
6. Automatically saves analysis results to CSV files:
   - `top_products.csv` → top 5 products by revenue.
   - `monthly_revenue.csv` → revenue per month.

---

## 📈 How to Run
1. Clone the repository:
   ```
   git clone <>
````

2. Make sure you have Python and required libraries installed:

   ```bash
   pip install pandas matplotlib
   ```
3. Place `sales_data.csv` in the project folder.
4. Run the script:

   ```bash
   python sales_data_analyzer.py
   ```
5. View the charts and check the generated CSV outputs (`top_products.csv` and `monthly_revenue.csv`).

---

## 🔍 Insights

* Quickly identifies which products generate the most revenue.
* Shows month-by-month revenue trends for better business decisions.
* Outputs are automatically generated, making analysis effortless.

---

## ⚡ Future Improvements

* Add interactive visualizations with **Plotly** or **Dash**.
* Include profit and discount analysis.
* Create a dashboard for different product categories and regions.

---

## 📂 File Structure


sales-data-analyzer/
│
├─ sales_data_analyzer.py
├─ sales_data.csv
├─ top_products.csv        # generated after running the script
├─ monthly_revenue.csv     # generated after running the script
└─ README.md


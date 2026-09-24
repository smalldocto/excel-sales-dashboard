# E-Commerce Sales Dashboard

An interactive Excel dashboard built to analyze e-commerce sales performance across products, countries, categories, and sales channels.

## 📊 Project Overview

This project transforms a 1,000-transaction e-commerce dataset into an interactive business dashboard using Microsoft Excel.

The dashboard allows users to monitor key performance indicators, explore sales trends, compare products and countries, and filter results interactively using slicers.

## 🎯 Business Questions

The dashboard was designed to answer questions such as:

- What are the total sales and total profit?
- What is the average order value?
- How are sales and profit changing over time?
- Which products generate the most sales?
- Which countries generate the most profit?
- Which sales channels generate the most revenue?
- How does performance change across different product categories?
- How do different countries and sales channels affect overall performance?

## 📈 Dashboard Features

### KPI Metrics

- Total Sales
- Total Profit
- Total Orders
- Average Order Value

### Interactive Visualizations

- Monthly Sales & Profit
- Sales by Product
- Profit by Country
- Sales by Sales Channel

### Interactive Filters

The dashboard includes slicers for:

- Country
- Sales Channel
- Category

Selecting a filter automatically updates the dashboard's PivotTables and charts.

## 🗂️ Dataset

The dataset contains **1,000 fictional e-commerce transactions** created for portfolio and analytical practice.

The dataset includes:

- Order ID
- Order Date
- Customer
- Country
- Region
- Product
- Category
- Quantity
- Unit Price
- Discount
- Sales
- Cost
- Profit
- Payment Method
- Sales Channel

## 🛠️ Excel Skills Demonstrated

This project demonstrates practical skills including:

- Excel Tables
- PivotTables
- PivotCharts
- Slicers
- Excel formulas
- KPI calculations
- Data aggregation
- Profit analysis
- Sales trend analysis
- Business dashboard design
- Interactive filtering
- Data visualization

## 📁 Project Structure

```text
excel-sales-dashboard/
│
├── Ecommerce_Sales_Dashboard.xlsx
├── ecommerce_sales_data.csv
├── generate_data.py
├── .gitignore
└── README.md 
🧮 Key Calculations
Total Sales
SUM(Sales)
Total Profit
SUM(Profit)
Total Orders
COUNT(Order ID)
Average Order Value
AVERAGE(Sales)
💡 Business Value

The dashboard provides a simple way for a business stakeholder to monitor sales performance and identify differences across products, countries, categories, and sales channels.

The interactive slicers make it possible to investigate specific segments without manually filtering the underlying dataset.

⚠️ Data Disclaimer

The dataset is fictional and was generated specifically for this portfolio project. It does not represent real company transactions or confidential business information.

🚀 Future Improvements

Potential improvements include:

Adding monthly growth KPIs
Adding profit margin analysis
Adding customer segmentation
Adding discount-performance analysis
Adding regional performance maps
Recreating the dashboard in Power BI
Connecting the dashboard to a live database
👤 Author

Mr Wayne

Aspiring Data Analyst focused on Excel, SQL, Python, data visualization, and business analytics.
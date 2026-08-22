<h1 align="center">Supply Chain & Logistics Analytics</h1>

<p align="center">
<b>A data analytics project that analyzes supply chain operations, delivery performance, inventory levels, shipping modes, and logistics efficiency using Python, MySQL, and Power BI.</b>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python">
    <img src="https://img.shields.io/badge/MySQL-Database-orange?style=flat-square&logo=mysql">
    <img src="https://img.shields.io/badge/Power%20BI-Analytics-yellow?style=flat-square&logo=powerbi">
    <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=flat-square&logo=pandas">
    <img src="https://img.shields.io/badge/NumPy-Data%20Processing-blue?style=flat-square&logo=numpy">
    <img src="https://img.shields.io/badge/Matplotlib-Visualization-green?style=flat-square">
</p>

<p align="center">
<strong>
<a href="#features">Features</a> •
<a href="#project-workflow">Workflow</a> •
<a href="#technology-stack">Tech Stack</a> •
<a href="#project-structure">Project Structure</a> •
<a href="#installation">Installation</a> •
<a href="#key-insights">Key Insights</a> •
<a href="#future-enhancements">Future Scope</a>
</strong>
</p>

---

# Supply Chain & Logistics Analytics

**Supply Chain & Logistics Analytics** is an end-to-end data analytics project designed to analyze and visualize supply chain operations.

The project processes supply chain data to identify patterns in **delivery performance, inventory availability, shipping modes, transportation costs, supplier performance, order quantities, and logistics efficiency**.

Python is used for data generation, preprocessing, exploratory data analysis, and visualization. MySQL is used for structured data storage and SQL analysis, while Power BI is used to build interactive dashboards and business intelligence reports.

---

# Why Supply Chain & Logistics Analytics?

Efficient supply chain management is essential for reducing operational costs, improving delivery performance, maintaining optimal inventory levels, and increasing customer satisfaction.

Organizations need to understand:

* Which shipments are delayed?
* Which products require inventory replenishment?
* Which shipping modes are most efficient?
* Which suppliers perform better?
* Where are transportation costs increasing?
* What factors contribute to delivery delays?
* How can inventory and logistics operations be optimized?

This project provides data-driven insights to help answer these questions.

---

# Features

* 📦 Supply Chain Dataset Generation
* 🧹 Data Cleaning and Preprocessing
* 🔍 Exploratory Data Analysis
* 📊 Delivery Performance Analysis
* 🚚 Shipping Mode Analysis
* 📦 Inventory Level Analysis
* 🏭 Supplier Performance Analysis
* 💰 Cost and Revenue Analysis
* ⏱ Delivery Delay Analysis
* 🗄 MySQL Database Integration
* 📈 Power BI Interactive Dashboard
* 📑 Automated Analysis Reports
* 📊 Business KPI Analysis

---

# Project Workflow

```text
Supply Chain Dataset
        │
        ▼
Data Generation
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Exploratory Data Analysis
        │
        ├───────────────┐
        ▼               ▼
Python Analysis      MySQL Database
        │               │
        └───────┬───────┘
                ▼
        SQL Data Analysis
                │
                ▼
        Power BI Dashboard
                │
                ▼
       Business Insights
                │
                ▼
       Decision Support
```

---

# Technology Stack

## Programming & Data Analysis

* Python 3.11
* Pandas
* NumPy
* Power BI

## Database

* MySQL
* SQL

## Business Intelligence

* Microsoft Power BI

## Development Tools

* Visual Studio Code
* Git
* GitHub

---

# Project Structure

```text
Supply_Chain_Logistics_Analytics/
│
├── data/
│   └── supply_chain.csv
│
├── powerbi/
│   └── Supply_Chain_Logistics_Dashboard.pbix
│
├── python/
│   ├── generate_dataset.py
│   └── eda.py
│
├── reports/
│   ├── charts/
│   └── analysis/
│
├── sql/
│   └── database_setup.sql
│
├── venv/
│
├── requirements.txt
│
└── README.md
```

---

# Dataset

The project uses a supply chain dataset containing **10,000 records and 28 columns**.

The dataset contains information related to:

* Product details
* Order information
* Customer information
* Supplier information
* Inventory
* Shipping
* Delivery
* Transportation
* Costs
* Revenue
* Delivery status

### Dataset Statistics

| Metric               |  Value |
| -------------------- | -----: |
| Total Records        | 10,000 |
| Total Columns        |     28 |
| On-Time Deliveries   |  7,915 |
| Delayed Deliveries   |  2,085 |
| Inventory Sufficient |  8,087 |
| Reorder Required     |  1,913 |

---

# Data Analysis

Python is used to perform exploratory data analysis and generate visualizations.

The analysis includes:

### Delivery Analysis

* On-time vs delayed deliveries
* Delivery performance by shipping mode
* Average delivery time
* Delay patterns

### Inventory Analysis

* Sufficient vs insufficient inventory
* Products requiring reorder
* Inventory levels
* Stock availability

### Shipping Analysis

* Shipping mode distribution
* Shipping costs
* Transportation performance
* Shipping mode comparison

### Supplier Analysis

* Supplier performance
* Supplier contribution
* Delivery performance by supplier

### Financial Analysis

* Revenue
* Product cost
* Shipping cost
* Profit-related metrics
* Operational cost analysis

---

# Exploratory Data Analysis

The `eda.py` script generates multiple charts and analysis files.

Example visualizations include:

```text
Delivery Status Analysis
        │
        ├── On-Time Deliveries
        └── Delayed Deliveries

Inventory Analysis
        │
        ├── Inventory Sufficient
        └── Reorder Required

Shipping Analysis
        │
        ├── Shipping Mode
        └── Shipping Performance

Supplier Analysis
        │
        └── Supplier Performance
```

Generated charts are stored inside:

```text
reports/charts/
```

Generated analysis files are stored inside:

```text
reports/analysis/
```

---

# MySQL Database

MySQL is used to store and analyze the supply chain dataset.

The database setup includes:

* Database creation
* Table creation
* Data loading
* SQL queries
* Aggregations
* Supply chain KPI analysis

Example SQL analysis:

```sql
SELECT
    delivery_status,
    COUNT(*) AS total_orders
FROM supply_chain
GROUP BY delivery_status;
```

---

# Power BI Dashboard

The Power BI dashboard provides an interactive view of the supply chain operations.

The dashboard can be used to analyze:

* Total Orders
* Total Revenue
* Total Cost
* Average Delivery Time
* On-Time Delivery Rate
* Delayed Orders
* Inventory Status
* Shipping Mode
* Supplier Performance

### Dashboard Analysis

Users can interact with the dashboard using filters and slicers to analyze supply chain performance across different dimensions.

Possible filters include:

* Product
* Supplier
* Shipping Mode
* Delivery Status
* Inventory Status
* Location
* Date

---

# Key Performance Indicators

The project focuses on important supply chain KPIs such as:

| KPI                    | Purpose                                  |
| ---------------------- | ---------------------------------------- |
| Total Orders           | Measures overall order volume            |
| On-Time Delivery Rate  | Measures delivery reliability            |
| Delayed Orders         | Identifies delivery problems             |
| Average Delivery Time  | Measures logistics efficiency            |
| Inventory Availability | Measures stock sufficiency               |
| Reorder Rate           | Identifies inventory replenishment needs |
| Shipping Cost          | Measures transportation expenses         |
| Revenue                | Measures business performance            |
| Supplier Performance   | Evaluates supplier efficiency            |

---

# Key Insights

Based on the generated dataset:

* **79.15%** of deliveries were completed on time.
* **20.85%** of deliveries were delayed.
* **80.87%** of inventory records showed sufficient inventory.
* **19.13%** of records required inventory reordering.
* Shipping modes can be compared to identify operational efficiency.
* Inventory analysis can help identify products that require timely replenishment.
* Delivery analysis can help identify areas where logistics performance can be improved.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/Supply_Chain_Logistics_Analytics.git
```

```bash
cd Supply_Chain_Logistics_Analytics
```

---

# Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Generate Dataset

Run the dataset generation script:

```bash
python python/generate_dataset.py
```

The script generates the supply chain dataset and saves it as:

```text
data/supply_chain.csv
```

---

# Run Exploratory Data Analysis

Execute:

```bash
python python/eda.py
```

The script generates:

* Data analysis results
* Statistical summaries
* Visualization charts
* CSV analysis reports

The generated files are stored in:

```text
reports/
```

---

# MySQL Setup

Make sure MySQL Server is installed and running.

Create the database and tables using:

```bash
mysql -u root -p < sql/database_setup.sql
```

Alternatively, in PowerShell:

```powershell
Get-Content ./sql/database_setup.sql | mysql -u root -p
```

Enter your MySQL password when prompted.

---

# Power BI Setup

1. Open **Power BI Desktop**.
2. Select **Get Data**.
3. Connect to the MySQL database or import the CSV dataset.
4. Load the supply chain data.
5. Create required relationships and measures.
6. Build charts and KPI cards.
7. Add slicers for interactive filtering.
8. Save the Power BI report.

The Power BI report can be stored in:

```text
powerbi/
```

---

# Example Dashboard Components

The Power BI dashboard can contain:

```text
┌──────────────────────────────────────────────────────┐
│          SUPPLY CHAIN LOGISTICS DASHBOARD            │
├────────────┬────────────┬────────────┬───────────────┤
│ Total      │ On-Time    │ Delayed    │ Inventory     │
│ Orders     │ Delivery % │ Orders     │ Availability  │
├────────────┴────────────┴────────────┴───────────────┤
│                                                      │
│        Delivery Performance Analysis                 │
│                                                      │
├─────────────────────────┬────────────────────────────┤
│ Shipping Mode Analysis   │ Inventory Analysis        │
│                         │                            │
├─────────────────────────┴────────────────────────────┤
│             Supplier Performance                     │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

# Business Applications

This project can be applied to:

* Supply chain management
* Logistics optimization
* Inventory management
* Warehouse management
* Transportation analysis
* Supplier evaluation
* Delivery performance monitoring
* Business intelligence
* Operational decision making

---

# Learning Outcomes

Through this project, the following skills are demonstrated:

* Python programming
* Data cleaning
* Data preprocessing
* Exploratory Data Analysis
* Data visualization
* SQL database management
* SQL querying
* Power BI dashboard development
* KPI development
* Business analytics
* Data-driven decision making

---

# Future Enhancements

* 🤖 Machine Learning-based Delivery Delay Prediction
* 📦 Demand Forecasting
* 🔮 Inventory Demand Prediction
* 🚚 Route Optimization
* 💰 Supply Chain Cost Prediction
* 📈 Advanced Supplier Risk Analysis
* ☁ Cloud Database Integration
* 🔄 Automated Data Pipeline
* 📊 Real-Time Supply Chain Dashboard
* 🤖 AI-Based Supply Chain Optimization
* 🌐 Power BI Service Deployment
* 📱 Mobile-Friendly Analytics Dashboard

---

# Conclusion

**Supply Chain & Logistics Analytics** demonstrates how data analytics and business intelligence can be used to understand and improve supply chain operations.

By combining **Python, MySQL, SQL, and Power BI**, the project transforms raw supply chain data into meaningful visualizations, KPIs, and business insights that can support better operational and strategic decisions.

---

# Author

**Pratthima**

AI & Data Science Student


---

This project is licensed under the **MIT License**.

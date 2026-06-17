# E-Commerce Sales Analytics & Data Warehouse Platform

## Project Overview

This project is an end-to-end Data Engineering and Business Intelligence solution built using the Brazilian E-Commerce Public Dataset (Olist). The system extracts raw e-commerce data, performs data profiling and transformation, designs a dimensional data warehouse using a Star Schema model, loads data into PostgreSQL, and delivers business insights through interactive Metabase dashboards.

The project simulates a real-world analytics platform used by e-commerce organizations to monitor sales performance, customer behavior, product trends, and seller performance.

---

## Business Problem

E-commerce companies generate large volumes of transactional data from customers, products, sellers, and orders. Raw data alone does not provide meaningful insights for business decision-making.

The goal of this project is to:

* Build a scalable data pipeline
* Clean and transform raw transactional data
* Design a data warehouse for analytics
* Generate business KPIs
* Visualize insights using dashboards

---

## Dataset

**Dataset:** Brazilian E-Commerce Public Dataset by Olist

The dataset contains information about:

* Customers
* Orders
* Products
* Sellers
* Payments
* Order Reviews

Key Metrics:

* 100,000+ Orders
* Multiple Product Categories
* Customer and Seller Information
* Historical Sales Transactions

---

## Solution Architecture

Raw CSV Files
↓
Data Profiling & Validation
↓
Data Cleaning & Transformation
↓
Star Schema Data Modeling
↓
PostgreSQL Data Warehouse
↓
Business KPI Layer
↓
Metabase Dashboard
↓
Business Insights

---

## Data Warehouse Design

### Fact Table

#### fact_orders

Stores transactional sales data.

Columns:

* order_id
* customer_id
* product_id
* seller_id
* order_date
* revenue

---

### Dimension Tables

#### dim_customer

* customer_id
* customer_unique_id
* city
* state
* customer_key

#### dim_product

* product_id
* category
* weight_g

#### dim_seller

* seller_id
* city
* state

#### dim_date

* date
* year
* month
* quarter

---

## Technology Stack

### Programming

* Python 3.11

### Data Processing

* Pandas
* NumPy

### Database

* PostgreSQL

### Visualization

* Metabase

### Containerization

* Docker
* Docker Compose

### Development Environment

* Jupyter Notebook
* VS Code

### Version Control

* Git
* GitHub

---

## Project Structure

```text
E-Commerce_Sales_Analytics_Pipeline

│
├── data
│   ├── raw
│   ├── processed
│   └── warehouse
│
├── notebooks
│   ├── data_understanding.ipynb
│   ├── business_analysis.ipynb
│   ├── data_modelling_warehouse.ipynb
│   ├── postgresql_loading.ipynb
│   └── business_kpis.ipynb
│
├── scripts
│   ├── extract.py
│   ├── validate.py
│   ├── transform.py
│   ├── load.py
│   └── etl_pipeline.py
│
├── sql
│   ├── schema.sql
│   └── kpis.sql
│
├── outputs
│   ├── dashboard.png
│   ├── revenue_analysis.png
│   └── seller_analysis.png
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ETL Pipeline

### Extract

* Load raw CSV datasets
* Validate source files
* Profile datasets

### Transform

* Handle missing values
* Remove duplicates
* Standardize categorical values
* Convert date formats
* Create business features

### Load

* Create dimensional tables
* Create fact table
* Load warehouse tables into PostgreSQL

---

## Business KPIs

### Executive Metrics

* Total Revenue
* Total Orders
* Total Customers
* Average Order Value

### Revenue Analysis

* Monthly Revenue Trend
* Revenue by State
* Revenue by City

### Product Analysis

* Revenue by Product Category
* Category Revenue Contribution

### Seller Analysis

* Top Sellers by Revenue
* Top Sellers by Order Volume

### Customer Analysis

* Top Customers by Revenue
* Top Customers by Orders

---

## Dashboard Features

### Executive Dashboard

* Revenue Overview
* Customer Overview
* Order Overview
* Average Order Value

### Revenue Dashboard

* Monthly Revenue Trends
* Revenue by State
* Revenue by City

### Product Dashboard

* Top Categories
* Category Contribution

### Seller Dashboard

* Top Performing Sellers

---

## Key Engineering Concepts Implemented

### Data Engineering

* ETL Pipeline
* Data Validation
* Data Cleaning
* Data Transformation
* Data Warehouse Design
* Star Schema Modeling
* Fact and Dimension Tables

### Database

* PostgreSQL
* SQL Query Optimization
* Analytical Queries

### Business Intelligence

* KPI Development
* Dashboard Design
* Data Visualization

### DevOps

* Docker
* Docker Compose

---

## Results

* Processed 100K+ e-commerce transactions
* Built an end-to-end ETL pipeline
* Designed a Star Schema Data Warehouse
* Loaded analytical datasets into PostgreSQL
* Developed multiple business KPIs
* Created interactive Metabase dashboards
* Generated actionable business insights

---

This is the Beginner level project of Data Engineering/Data Analytics

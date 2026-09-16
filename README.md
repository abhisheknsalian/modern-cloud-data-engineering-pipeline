# 🚀 Modern Cloud Data Engineering Pipeline

![Python](https://img.shields.io/badge/Python-3.12-blue)
![AWS S3](https://img.shields.io/badge/AWS-S3-orange)
![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Warehouse-blue)
![dbt](https://img.shields.io/badge/dbt-Analytics%20Engineering-orange)
![Terraform](https://img.shields.io/badge/Terraform-IaC-purple)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)

An end-to-end modern cloud data engineering platform built around the **Online Retail II dataset**, demonstrating batch ETL, data quality, cloud storage, data warehousing, analytics engineering, infrastructure as code, CI validation, containerization, and interactive analytics.

---

## 📌 Project Overview

This project demonstrates an end-to-end data engineering workflow using industry-standard technologies and architectural patterns.

The pipeline processes more than **1 million retail transactions** from the Online Retail II dataset and transforms raw transactional data into analytics-ready datasets.

The project follows a **Medallion Architecture**:

```text
Raw Data
   │
   ▼
Python ETL Pipeline
   │
   ▼
┌──────────────┐
│ Bronze Layer │
│ Raw Data     │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Silver Layer │
│ Clean Data   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Gold Layer  │
│ Analytics    │
└──────┬───────┘
       │
       ├──────────────► Amazon S3
       │
       ▼
┌──────────────────┐
│    Snowflake     │
│  Data Warehouse  │
└────────┬─────────┘
         │
         ▼
        dbt
         │
         ▼
┌──────────────────┐
│ Analytics Models │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│    Streamlit     │
│    Dashboard     │
└──────────────────┘
````

Infrastructure and development automation are handled using:

```text
Terraform
    +
GitHub Actions
    +
Docker
```

---

# ✨ Key Features

* End-to-end batch ETL pipeline using Python
* Medallion Architecture: Bronze → Silver → Gold
* Data validation and quality checks
* Parquet-based analytical datasets
* Amazon S3 data lake integration
* Snowflake cloud data warehouse
* dbt analytics engineering models
* Star-schema analytical modeling
* Terraform Infrastructure as Code
* GitHub Actions CI pipeline
* Docker-based development environment
* Interactive Streamlit analytics dashboard
* Customer, product, country, and sales analytics
* Pipeline status and data-quality visibility

---

# 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │  Online Retail II    │
                    │      Dataset         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Python ETL        │
                    │ Extract / Validate   │
                    │ Transform / Load     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Bronze Layer      │
                    │   Raw Parquet Data   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Silver Layer      │
                    │   Cleaned Data       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Gold Layer       │
                    │ Analytics Datasets   │
                    └───────┬───────┬──────┘
                            │       │
                            │       └──────────────┐
                            ▼                      ▼
                    ┌──────────────┐       ┌──────────────┐
                    │  Amazon S3   │       │  Streamlit   │
                    │  Data Lake   │       │  Dashboard   │
                    └───────┬──────┘       └──────────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │  Snowflake   │
                    │ Data Warehouse│
                    └──────┬───────┘
                           │
                           ▼
                         dbt
                           │
                           ▼
                    ┌──────────────┐
                    │ Analytics    │
                    │ Data Models  │
                    └──────────────┘

       Terraform ─────► Infrastructure as Code
       GitHub Actions ─► CI Validation
       Docker ─────────► Reproducible Environment
```

---

# 📊 Dataset

The project uses the **Online Retail II** dataset.

The dataset contains retail transactions recorded between **2009 and 2011**.

The processed dataset contains approximately:

```text
1,067,371 transactions
43 countries
5,698 products
5,942 customers
```

The raw dataset is stored under:

```text
data/raw/
```

---

# 🔄 ETL Pipeline

The Python pipeline is responsible for the initial data engineering workflow.

## Pipeline Flow

```text
Extract
   ↓
Validate
   ↓
Transform
   ↓
Bronze
   ↓
Silver
   ↓
Gold
```

## Extract

The raw Excel dataset is loaded into Pandas.

Main module:

```text
scripts/extract.py
```

## Validate

The pipeline performs data-quality checks including:

* Missing values
* Duplicate records
* Negative quantities
* Negative prices
* Missing customer identifiers
* Missing descriptions

Main module:

```text
scripts/validate.py
```

## Transform

Raw transactional data is cleaned and transformed into an analytics-friendly structure.

Main module:

```text
scripts/transform.py
```

## Load

Processed datasets are written as Parquet files.

Main module:

```text
scripts/load.py
```

## Gold Transformations

Business-oriented analytical tables are generated from the cleaned data.

Main module:

```text
scripts/gold.py
```

---

# 🥉 Bronze Layer

The Bronze layer stores the extracted raw data in Parquet format.

```text
data/bronze/
└── retail_raw.parquet
```

Purpose:

* Preserve extracted data
* Provide a reproducible intermediate layer
* Separate raw ingestion from transformation

---

# 🥈 Silver Layer

The Silver layer contains cleaned and transformed data.

```text
data/silver/
└── retail_cleaned.parquet
```

Processing includes:

* Data type normalization
* Missing-value handling
* Duplicate handling
* Invalid transaction filtering
* Revenue calculations
* Column standardization

---

# 🥇 Gold Layer

The Gold layer contains business-ready analytical datasets.

```text
data/gold/
├── monthly_sales.parquet
├── country_sales.parquet
├── customer_summary.parquet
└── top_products.parquet
```

### Monthly Sales

Used for:

* Revenue trends
* Monthly performance
* Time-series analysis

### Country Sales

Used for:

* Geographic analysis
* Revenue by country
* Country-level comparisons

### Customer Summary

Used for:

* Customer revenue
* Customer-level analytics
* Top customer analysis

### Top Products

Used for:

* Product performance
* Revenue analysis
* Best-selling products

---

# ☁️ Amazon S3

Amazon S3 is used as the cloud data lake layer.

The project organizes data into:

```text
S3 Bucket
│
├── bronze/
├── silver/
├── gold/
└── reports/
```

This mirrors the local Medallion Architecture.

---

# ❄️ Snowflake

Snowflake is used as the cloud data warehouse.

The warehouse structure is:

```text
RETAIL_DB
│
├── RAW
├── STAGING
└── MARTS
```

The pipeline loads retail data into Snowflake and uses SQL/dbt for analytical modeling.

---

# 🔧 dbt Analytics Engineering

dbt is used to transform warehouse data into reusable analytical models.

The dbt project is located at:

```text
retail_dbt/
```

## Staging Model

```text
models/staging/stg_retail.sql
```

The staging layer provides a clean interface over the raw warehouse table.

## Mart Models

```text
models/marts/
├── fact_sales.sql
├── dim_customer.sql
├── dim_product.sql
└── dim_date.sql
```

The resulting analytical structure follows a dimensional/star-schema approach:

```text
                 dim_customer
                      │
                      │
dim_product ──── fact_sales ──── dim_date
```

This allows downstream analytics to work with business-oriented models instead of raw transactional data.

---

# 🏗️ Terraform Infrastructure as Code

Terraform is used to define the AWS infrastructure required by the project.

Terraform configuration:

```text
terraform/
├── provider.tf
├── variables.tf
├── terraform.tfvars
├── main.tf
├── outputs.tf
└── .gitignore
```

The infrastructure definition includes:

* Amazon S3 bucket
* S3 versioning
* Server-side AES256 encryption
* Project tagging

Terraform was successfully initialized, formatted, validated, and planned using:

```bash
terraform init
terraform fmt
terraform validate
terraform plan
```

The Terraform configuration was validated successfully.

> Note: Terraform infrastructure was defined and planned, but `terraform apply` was not performed in the development environment because of AWS Academy credential/permission limitations.

---

# ⚙️ GitHub Actions CI

The project includes a GitHub Actions workflow:

```text
.github/workflows/ci.yml
```

The CI pipeline performs:

```text
Checkout Repository
        ↓
Set up Python
        ↓
Install Dependencies
        ↓
Run ETL Pipeline
        ↓
Set up Terraform
        ↓
Terraform Format Check
        ↓
Terraform Initialize
        ↓
Terraform Validate
```

The workflow automatically validates the Python ETL pipeline and Terraform configuration whenever changes are pushed to `main` or submitted through a pull request.

> The current GitHub Actions workflow is focused on continuous integration and validation. It does not automatically deploy cloud infrastructure or application code.

---

# 🖥️ Streamlit Analytics Dashboard

The project includes an interactive Streamlit dashboard built on top of the Gold analytical datasets.

Run the dashboard with:

```bash
streamlit run app/app.py
```

The dashboard provides several analytical views.

## Overview

The Overview page displays:

* Total Revenue
* Total Customers
* Countries
* Products
* Revenue Trend
* Platform Architecture

Example metrics from the processed Gold datasets:

```text
Total Revenue    €19.23M
Customers        5,942
Countries        43
Products         5,698
```

## Sales Analytics

The Sales Analytics page provides:

* Monthly sales
* Revenue trends
* Sales metrics
* Time-based analysis

## Customer Analytics

The Customer Analytics page provides:

* Total customers
* Customer revenue
* Customer summary
* Top customers by revenue

## Product Analytics

The Product Analytics page provides:

* Product performance
* Revenue by product
* Top products
* Product-level analysis

## Data Quality

The dashboard surfaces data-quality results from the ETL validation process.

Example validation results:

```text
Countries                 43
Duplicate Rows            12,133
Missing Customer ID       243,007
Missing Description       4,382
Negative Price            5
Negative Quantity         229
```

## Pipeline Status

The dashboard provides an engineering-oriented view of the pipeline:

```text
Extract       ✓
Validate      ✓
Transform     ✓
Bronze        ✓
Silver        ✓
Gold          ✓
```

---

# 📁 Project Structure

```text
modern-cloud-data-engineering-pipeline/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── logs/
│
├── reports/
│
├── retail_dbt/
│   ├── models/
│   │   ├── staging/
│   │   ├── intermediate/
│   │   └── marts/
│   ├── schema.yml
│   └── dbt_project.yml
│
├── scripts/
│   ├── config.py
│   ├── logger.py
│   ├── extract.py
│   ├── validate.py
│   ├── transform.py
│   ├── schema.py
│   ├── load.py
│   ├── gold.py
│   ├── upload_s3.py
│   ├── pipeline.py
│   └── main.py
│
├── terraform/
│   ├── provider.tf
│   ├── variables.tf
│   ├── terraform.tfvars
│   ├── main.tf
│   ├── outputs.tf
│   └── .gitignore
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🚀 Running the Project Locally

## 1. Clone the Repository

```bash
git clone git@github.com:abhisheknsalian/modern-cloud-data-engineering-pipeline.git

cd modern-cloud-data-engineering-pipeline
```

## 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If Streamlit is not already included in `requirements.txt`:

```bash
pip install streamlit
```

## 4. Run the ETL Pipeline

```bash
python -m scripts.main
```

The pipeline generates:

```text
data/bronze/
data/silver/
data/gold/
```

## 5. Run the Streamlit Dashboard

```bash
streamlit run app/app.py
```

Then open:

```text
http://localhost:8501
```

---

# 🐳 Docker

Docker configuration is included to support reproducible development and execution.

Build the Docker image:

```bash
docker build -t modern-data-pipeline .
```

Run using Docker Compose:

```bash
docker compose up
```

---

# 🧪 Data Quality

The pipeline incorporates validation before downstream transformation.

Example validation results:

| Check               |  Result |
| ------------------- | ------: |
| Countries           |      43 |
| Duplicate rows      |  12,133 |
| Missing Customer ID | 243,007 |
| Missing Description |   4,382 |
| Negative Price      |       5 |
| Negative Quantity   |     229 |

The purpose of these checks is to identify source-data issues before downstream analytical processing.

---

# 🛠️ Technology Stack

## Data Engineering

* Python
* Pandas
* NumPy
* Parquet
* ETL
* Data Validation

## Cloud

* Amazon S3
* Snowflake

## Analytics Engineering

* SQL
* dbt
* Dimensional Modeling
* Star Schema

## Infrastructure

* Terraform
* Infrastructure as Code

## DevOps

* Git
* GitHub
* GitHub Actions
* Docker

## Visualization

* Streamlit
* Plotly

---

# 🎯 Engineering Concepts Demonstrated

This project demonstrates practical implementation of:

* Batch data pipelines
* ETL architecture
* Medallion Architecture
* Data Lake concepts
* Cloud Data Warehousing
* Dimensional Modeling
* Fact and Dimension tables
* Data Quality
* SQL transformations
* Analytics Engineering
* Infrastructure as Code
* Continuous Integration
* Containerization
* Data Visualization
* Cloud Architecture

---

# 🔮 Future Improvements

Potential future extensions include:

* Apache Airflow orchestration
* AWS Glue integration
* Amazon Athena
* Incremental dbt models
* dbt tests and documentation
* Data lineage
* CloudWatch monitoring
* Automated data-quality alerts
* Snowflake task scheduling
* Production CI/CD deployment
* Role-based access control
* Dashboard authentication
* Connecting Streamlit directly to Snowflake

---

# 📈 Project Outcome

The final platform demonstrates how raw transactional data can be transformed into a complete analytics ecosystem:

```text
Raw Data
   ↓
Python ETL
   ↓
Data Quality
   ↓
Bronze
   ↓
Silver
   ↓
Gold
   ↓
Amazon S3
   ↓
Snowflake
   ↓
dbt
   ↓
Analytics Models
   ↓
Streamlit Dashboard
```

Terraform provides infrastructure-as-code capabilities, while GitHub Actions automatically validates the codebase and infrastructure configuration.

The project demonstrates the complete lifecycle of a modern data engineering workflow, from raw data ingestion through transformation, cloud storage, warehousing, analytics modeling, and visualization.

---

# 👨‍💻 Author

**Abhishek Nagesh Salian**

M.Sc. Data Science
Berlin, Germany

**GitHub:**
[https://github.com/abhisheknsalian](https://github.com/abhisheknsalian)

**LinkedIn:**
[https://www.linkedin.com/in/abhishek-salian-13b3091a5/](https://www.linkedin.com/in/abhishek-salian-13b3091a5/)

---

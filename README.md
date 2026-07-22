# 🚀 Modern Cloud Data Engineering Pipeline

![Python](https://img.shields.io/badge/Python-3.12-blue)
![AWS](https://img.shields.io/badge/AWS-S3-orange)
![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Warehouse-blue)
![dbt](https://img.shields.io/badge/dbt-Analytics%20Engineering-orange)
![Terraform](https://img.shields.io/badge/Terraform-IaC-purple)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-success)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)

---

## 📌 Project Overview

This project demonstrates an end-to-end modern cloud data engineering pipeline built using industry-standard tools and best practices.

The pipeline extracts raw retail transaction data, validates and transforms it into a Medallion Architecture (Bronze, Silver, Gold), stores datasets in Amazon S3, models analytical tables in Snowflake using dbt, provisions cloud infrastructure with Terraform, and automates validation using GitHub Actions.

The objective of this project is to simulate a production-grade data engineering workflow while showcasing cloud infrastructure, analytics engineering, DevOps, and ETL development skills.

---

# ✨ Key Features

- End-to-end batch ETL pipeline using Python
- Medallion Architecture (Bronze, Silver, Gold)
- Data Lake implementation with Amazon S3
- Cloud Data Warehouse using Snowflake
- Analytics Engineering with dbt
- Infrastructure as Code using Terraform
- Automated CI pipeline with GitHub Actions
- Dockerized development environment
- Data validation and quality checks

# 🏗 Architecture

```
                    Online Retail Dataset
                             │
                             ▼
                  Python ETL Pipeline
                             │
          ┌──────────────────┼──────────────────┐
          ▼                  ▼                  ▼
      Bronze Layer      Silver Layer      Gold Layer
                             │
                             ▼
                       Amazon S3 Data Lake
                             │
                             ▼
                    Snowflake Data Warehouse
                             │
                             ▼
                        dbt Transformations
                             │
                             ▼
                    Analytics Ready Tables
                             │
                             ▼
                  GitHub Actions CI Pipeline
```

---

# 📂 Project Structure

```
modern-cloud-data-engineering-pipeline/

│
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── scripts/
│
├── retail_dbt/
│
├── terraform/
│
├── .github/workflows/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# ⚙ Technologies Used

- Python
- Pandas
- NumPy
- AWS S3
- Snowflake
- dbt
- Terraform
- GitHub Actions
- Docker
- Git
- SQL
- Parquet

---

# 🚀 Pipeline Workflow

## Phase 1 – Python ETL

- Extract raw retail transactions
- Data validation
- Data cleaning
- Generate Bronze layer
- Generate Silver layer
- Generate Gold layer

Outputs:

- Monthly Sales
- Country Sales
- Customer Summary
- Top Products

---

## Phase 2 – Amazon S3

- Configure AWS S3
- Upload Bronze Layer
- Upload Silver Layer
- Upload Gold Layer
- Store validation reports

---

## Phase 3 – Snowflake

- Create warehouse
- Create database
- Create schemas
- Load datasets
- Build analytical warehouse

---

## Phase 4 – dbt

Built analytical models:

- stg_retail
- fact_sales
- dim_customer
- dim_product
- dim_date

Implemented:

- Source configuration
- Materializations
- Star Schema
- Analytics-ready marts

---

## Phase 5 – Terraform

Infrastructure as Code:

- AWS Provider
- Secure S3 Bucket
- Versioning
- Encryption
- Infrastructure Validation

---

## Phase 6 – GitHub Actions

Continuous Integration pipeline automatically:

- Checks out repository
- Installs dependencies
- Executes Python ETL
- Validates Terraform
- Reports build status

---

# 🔄 End-to-End Data Flow

```
Raw Dataset

↓

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

↓

Amazon S3

↓

Snowflake

↓

dbt

↓

Analytics Models
```

---

# ▶ Running the Project

## Clone Repository

```bash
git clone https://github.com/abhisheknsalian/modern-cloud-data-engineering-pipeline.git

cd modern-cloud-data-engineering-pipeline
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Execute ETL Pipeline

```bash
python scripts/main.py
```

## Run dbt

```bash
cd retail_dbt

dbt run
```

## Validate Terraform

```bash
cd terraform

terraform validate
```

---

# 📈 Outputs

The pipeline generates:

- Bronze Dataset
- Silver Dataset
- Gold Dataset
- Monthly Sales
- Country Sales
- Customer Summary
- Top Products

---

# 💡 Future Improvements

- Apache Airflow Orchestration
- AWS Glue Integration
- Amazon Athena Queries
- Power BI Dashboard
- Great Expectations Data Validation
- Docker Deployment
- Kubernetes
- CI/CD Deployment Pipeline

---

# 🎯 Skills Demonstrated

- Data Engineering
- Cloud Computing
- ETL Development
- Data Warehousing
- Analytics Engineering
- Infrastructure as Code
- DevOps
- CI/CD
- SQL
- Python
- Cloud Architecture

---

# 👨‍💻 Author

**Abhishek Nagesh Salian**

M.Sc. Data Science

University of Europe for Applied Sciences

Berlin, Germany

GitHub:

https://github.com/abhisheknsalian

LinkedIn:

https://www.linkedin.com/in/abhishek-salian-13b3091a5/

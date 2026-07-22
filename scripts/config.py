from dotenv import load_dotenv

load_dotenv()
from pathlib import Path

# Project root
ROOT_DIR = Path(__file__).resolve().parent.parent

# Data directories
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
BRONZE_DATA_DIR = ROOT_DIR / "data" / "bronze"
SILVER_DATA_DIR = ROOT_DIR / "data" / "silver"
GOLD_DATA_DIR = ROOT_DIR / "data" / "gold"

LOG_DIR = ROOT_DIR / "logs"
REPORT_DIR = ROOT_DIR / "reports"

# Input
RAW_DATASET = RAW_DATA_DIR / "online_retail_II.xlsx"

# Bronze
BRONZE_DATASET = BRONZE_DATA_DIR / "retail_raw.parquet"

# Silver
SILVER_DATASET = SILVER_DATA_DIR / "retail_cleaned.parquet"

# Reports
DATA_QUALITY_REPORT = REPORT_DIR / "data_quality_report.json"

# Create directories automatically
for directory in [
    BRONZE_DATA_DIR,
    SILVER_DATA_DIR,
    GOLD_DATA_DIR,
    LOG_DIR,
    REPORT_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)

# Gold datasets
MONTHLY_SALES = GOLD_DATA_DIR / "monthly_sales.parquet"
COUNTRY_SALES = GOLD_DATA_DIR / "country_sales.parquet"
TOP_PRODUCTS = GOLD_DATA_DIR / "top_products.parquet"
CUSTOMER_SUMMARY = GOLD_DATA_DIR / "customer_summary.parquet"
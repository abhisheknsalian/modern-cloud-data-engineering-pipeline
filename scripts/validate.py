import pandas as pd

from scripts.logger import logger


def validate_data(df: pd.DataFrame) -> dict:
    """
    Perform data quality validation and return summary statistics.
    """

    logger.info("Starting data validation...")

    report = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_values": df.isnull().sum().to_dict(),
        "negative_quantity": int((df["Quantity"] < 0).sum()),
        "negative_price": int((df["Price"] < 0).sum()),
        "unique_customers": df["Customer ID"].nunique(),
        "unique_products": df["StockCode"].nunique(),
        "countries": df["Country"].nunique(),
        "date_range": {
            "start": str(df["InvoiceDate"].min()),
            "end": str(df["InvoiceDate"].max()),
        },
    }

    logger.info("Validation completed.")

    return report
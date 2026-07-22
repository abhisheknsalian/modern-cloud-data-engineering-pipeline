import pandas as pd

from scripts.logger import logger


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform the retail dataset.
    """

    logger.info("Starting data transformation...")

    transformed_df = df.copy()

    # Convert invoice date
    transformed_df["InvoiceDate"] = pd.to_datetime(
        transformed_df["InvoiceDate"]
    )

    # Convert Invoice to string
    transformed_df["Invoice"] = transformed_df["Invoice"].astype(str)

    # Convert StockCode to string
    transformed_df["StockCode"] = transformed_df["StockCode"].astype(str)

    # Remove duplicate rows
    before = len(transformed_df)
    transformed_df = transformed_df.drop_duplicates()
    removed = before - len(transformed_df)

    logger.info(f"Removed {removed} duplicate rows.")

    # Create TotalPrice
    transformed_df["TotalPrice"] = (
        transformed_df["Quantity"] *
        transformed_df["Price"]
    )

    # Date features
    transformed_df["Year"] = transformed_df["InvoiceDate"].dt.year
    transformed_df["Month"] = transformed_df["InvoiceDate"].dt.month
    transformed_df["Quarter"] = transformed_df["InvoiceDate"].dt.quarter
    transformed_df["Weekday"] = transformed_df["InvoiceDate"].dt.day_name()

    # Cancelled invoices
    transformed_df["IsCancelled"] = (
        transformed_df["Invoice"]
        .astype(str)
        .str.startswith("C")
    )

    logger.info("Transformation completed.")

    return transformed_df
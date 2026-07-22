import pandas as pd

from scripts.config import (
    COUNTRY_SALES,
    CUSTOMER_SUMMARY,
    MONTHLY_SALES,
    TOP_PRODUCTS,
)
from scripts.logger import logger
from scripts.schema import enforce_schema


def generate_gold_tables(df: pd.DataFrame):
    """
    Generate Gold Layer business analytics tables.
    """

    logger.info("Generating Gold Layer...")

    # Monthly Sales
    monthly_sales = (
        df.groupby(["Year", "Month"], as_index=False)["TotalPrice"]
        .sum()
        .rename(columns={"TotalPrice": "Revenue"})
    )

    # Country Sales
    country_sales = (
        df.groupby("Country", as_index=False)["TotalPrice"]
        .sum()
        .sort_values("TotalPrice", ascending=False)
        .rename(columns={"TotalPrice": "Revenue"})
    )

    # Top Products
    top_products = (
        df.groupby(
            ["StockCode", "Description"],
            as_index=False,
        )["Quantity"]
        .sum()
        .sort_values("Quantity", ascending=False)
    )

    # Customer Summary
    customer_summary = (
        df.groupby("Customer ID", as_index=False)["TotalPrice"]
        .sum()
        .sort_values("TotalPrice", ascending=False)
        .rename(columns={"TotalPrice": "Revenue"})
    )

    # Enforce schema before saving
    monthly_sales = enforce_schema(monthly_sales)
    country_sales = enforce_schema(country_sales)
    top_products = enforce_schema(top_products)
    customer_summary = enforce_schema(customer_summary)

    # Save Gold tables
    monthly_sales.to_parquet(MONTHLY_SALES, index=False)
    country_sales.to_parquet(COUNTRY_SALES, index=False)
    top_products.to_parquet(TOP_PRODUCTS, index=False)
    customer_summary.to_parquet(CUSTOMER_SUMMARY, index=False)

    logger.info("Gold Layer generated successfully.")

    return {
        "monthly_sales": monthly_sales,
        "country_sales": country_sales,
        "top_products": top_products,
        "customer_summary": customer_summary,
    }
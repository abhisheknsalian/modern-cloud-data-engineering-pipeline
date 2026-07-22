import pandas as pd

from scripts.config import (
    BRONZE_DATASET,
    SILVER_DATASET,
)
from scripts.logger import logger
from scripts.schema import enforce_schema


def save_bronze(df: pd.DataFrame):

    logger.info("Saving Bronze dataset...")

    bronze_df = enforce_schema(df)

    bronze_df.to_parquet(
        BRONZE_DATASET,
        index=False,
    )

    logger.info(f"Saved: {BRONZE_DATASET}")


def save_silver(df: pd.DataFrame):

    logger.info("Saving Silver dataset...")

    silver_df = enforce_schema(df)

    silver_df.to_parquet(
        SILVER_DATASET,
        index=False,
    )

    logger.info(f"Saved: {SILVER_DATASET}")
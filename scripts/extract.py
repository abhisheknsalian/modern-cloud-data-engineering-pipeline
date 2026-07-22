import pandas as pd

from scripts.config import RAW_DATASET
from scripts.logger import logger


def extract_data() -> pd.DataFrame:
    """
    Read all sheets from the Online Retail II dataset
    and combine them into a single DataFrame.
    """

    logger.info(f"Reading dataset: {RAW_DATASET}")

    try:
        sheets = pd.read_excel(
            RAW_DATASET,
            sheet_name=None,
            engine="openpyxl"
        )

        logger.info(f"Found {len(sheets)} sheets.")

        dataframes = []

        for sheet_name, df in sheets.items():
            logger.info(
                f"Loaded sheet '{sheet_name}' with {len(df)} rows."
            )

            df["SourceSheet"] = sheet_name
            dataframes.append(df)

        combined_df = pd.concat(
            dataframes,
            ignore_index=True
        )

        logger.info(
            f"Combined dataset contains {len(combined_df)} rows."
        )

        return combined_df

    except Exception as e:
        logger.exception(f"Dataset extraction failed: {e}")
        raise
import pandas as pd


STRING_COLUMNS = [
    "Invoice",
    "StockCode",
    "Description",
    "Country",
    "SourceSheet",
]


def enforce_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply consistent data types across the pipeline.
    """

    df = df.copy()

    # Convert string columns
    for column in STRING_COLUMNS:
        if column in df.columns:
            df[column] = df[column].astype("string")

    # Convert numeric columns
    if "Quantity" in df.columns:
        df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

    if "Price" in df.columns:
        df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

    if "Customer ID" in df.columns:
        df["Customer ID"] = pd.to_numeric(df["Customer ID"], errors="coerce")

    # Convert dates
    if "InvoiceDate" in df.columns:
        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    return df
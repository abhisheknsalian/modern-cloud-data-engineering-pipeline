import os
from pathlib import Path

import boto3
from botocore.exceptions import ClientError

from scripts.logger import logger

# Read bucket name from environment variable
S3_BUCKET = os.getenv("S3_BUCKET")

# Create S3 client
s3 = boto3.client("s3")


def upload_directory(local_directory: str, s3_prefix: str):
    """
    Upload all files from a local directory to an S3 prefix.
    """

    local_directory = Path(local_directory)

    if not local_directory.exists():
        logger.warning(f"{local_directory} does not exist.")
        return

    for file in local_directory.rglob("*"):

        if file.is_file():

            s3_key = f"{s3_prefix}/{file.name}"

            try:

                s3.upload_file(
                    str(file),
                    S3_BUCKET,
                    s3_key,
                )

                logger.info(f"Uploaded {file.name} → s3://{S3_BUCKET}/{s3_key}")

            except ClientError as e:
                logger.error(e)


def upload_pipeline_outputs():
    """
    Upload Bronze, Silver, Gold and Reports folders.
    """

    logger.info("Uploading pipeline outputs to Amazon S3...")

    upload_directory("data/bronze", "bronze")
    upload_directory("data/silver", "silver")
    upload_directory("data/gold", "gold")
    upload_directory("reports", "reports")

    logger.info("Upload completed successfully.")
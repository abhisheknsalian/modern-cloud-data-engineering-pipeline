from pprint import pprint
from scripts.gold import generate_gold_tables

from scripts.extract import extract_data
from scripts.load import save_bronze, save_silver
from scripts.transform import transform_data
from scripts.validate import validate_data


def main():

    raw_df = extract_data()

    save_bronze(raw_df)

    report = validate_data(raw_df)

    print("\n========== DATA QUALITY REPORT ==========\n")

    pprint(report)

    silver_df = transform_data(raw_df)

    save_silver(silver_df)

    generate_gold_tables(silver_df)

    print("\nPipeline executed successfully.")

    


if __name__ == "__main__":
    main()
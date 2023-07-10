import argparse
from pathlib import Path

import pandas as pd

from life_expectancy.cleaning import DataCleaner
from life_expectancy.loading_saving import DataLoader, save_data

PARENT_PATH = Path(__file__).parent
FILE_PATH = PARENT_PATH / 'data'
OUTPUT_FILE_NAME = 'pt_life_expectancy.csv'
OUTPUT_FILE_PATH = FILE_PATH / OUTPUT_FILE_NAME


def main(file_format: str, region: str) -> pd.DataFrame:
    """
    Main function.
    Method that loads, cleans and saves data.

    Args:
    file_format [str]: file format (e.g. "csv", "json")
    region [str]: region to filter data.
    """

    data_df = DataLoader(file_format).load_data()

    cleaned_df = DataCleaner(file_format).clean_data(data_df, region)

    save_data(cleaned_df, OUTPUT_FILE_PATH)
    return cleaned_df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path')
    parser.add_argument('region')
    args = parser.parse_args()
    main(args.file_path, args.region)

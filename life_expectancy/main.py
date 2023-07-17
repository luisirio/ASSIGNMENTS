import argparse
from pathlib import Path

import pandas as pd

from life_expectancy.cleaning import DataCleanerJSON, DataCleanerTSV
from life_expectancy.loading_saving import (DataLoaderJSON, DataLoaderTSV,
                                            save_data)

PARENT_PATH = Path(__file__).parent
FILE_PATH = PARENT_PATH / 'data'
OUTPUT_FILE_NAME = 'pt_life_expectancy.csv'
OUTPUT_FILE_PATH = FILE_PATH / OUTPUT_FILE_NAME
TSV_FILE_NAME = 'eu_life_expectancy_raw.tsv'
JSON_FILE_NAME = 'eurostat_life_expect.json'
TSV_FILE_PATH = FILE_PATH / TSV_FILE_NAME
JSON_FILE_PATH = FILE_PATH / JSON_FILE_NAME


def main(file_format: str, region: str) -> pd.DataFrame:
    """
    Main function.
    Method that loads, cleans and saves data.

    Args:
    file_format [str]: file format (e.g. "csv", "json")
    region [str]: region to filter data.
    """

    if file_format == 'csv':
        file_path = TSV_FILE_PATH
        loader, cleaner = DataLoaderTSV(file_path), DataCleanerTSV()
    elif file_format == 'json':
        file_path = JSON_FILE_PATH
        loader, cleaner = DataLoaderJSON(file_path), DataCleanerJSON()

    df = loader.load_data()
    cleaned_df = cleaner.clean_data(df, region)

    save_data(cleaned_df, OUTPUT_FILE_PATH)
    return cleaned_df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_format')
    parser.add_argument('region')
    args = parser.parse_args()
    main(args.file_format, args.region)

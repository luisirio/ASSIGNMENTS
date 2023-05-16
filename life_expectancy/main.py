import argparse
from pathlib import Path

import pandas as pd

from life_expectancy.cleaning import clean_data
from life_expectancy.loading_saving import load_data, save_data

PARENT_PATH = Path(__file__).parent
FILE_PATH = PARENT_PATH / 'data'
INPUT_FILE_NAME = 'eu_life_expectancy_raw.tsv'
OUTPUT_FILE_NAME = 'pt_life_expectancy.csv'
INPUT_FILE_PATH = FILE_PATH / INPUT_FILE_NAME
OUTPUT_FILE_PATH = FILE_PATH / OUTPUT_FILE_NAME

def main(region: str) -> pd.DataFrame:
    """
    Main function.
    Method that loads, cleans and saves data.

    Args:
    region [str]: region to filter data.
    """
    data_df = load_data(INPUT_FILE_PATH)
    clean_df = clean_data(data_df, region)
    save_data(clean_df, OUTPUT_FILE_PATH)
    return clean_df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('region')
    args = parser.parse_args()
    main(args.region)
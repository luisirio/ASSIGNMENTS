import argparse

import pandas as pd

from life_expectancy.cleaning import clean_data
from life_expectancy.loading_saving import load_data, save_data


def main(region: str) -> pd.DataFrame:
    """
    Main function.
    Method that loads, cleans and saves data.
    """
    data_df = load_data()
    clean_df = clean_data(data_df, region)
    save_data(clean_df)
    return clean_df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('region')
    args = parser.parse_args()
    main(args.region)
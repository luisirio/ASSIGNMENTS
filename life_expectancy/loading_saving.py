"""
Module to load and save data
"""

from pathlib import Path

import pandas as pd

PARENT_PATH = Path(__file__).parent
FILE_PATH = PARENT_PATH / 'data'
TSV_FILE_NAME = 'eu_life_expectancy_raw.tsv'
JSON_FILE_NAME = 'eurostat_life_expect.json'
TSV_FILE_PATH = FILE_PATH / TSV_FILE_NAME
JSON_FILE_PATH = FILE_PATH / JSON_FILE_NAME


class DataLoader:
    """
    This class is responsible for verifying the format
    and assign the right load method
    """
    def __init__(self, data_format):
        self.data_format = data_format

    def load_csv(self) -> pd.DataFrame:
        """Method to load csv file"""
        return pd.read_csv(TSV_FILE_PATH, sep='\t')

    def load_json(self) -> pd.DataFrame:
        """Method to load json file"""
        return pd.read_json(JSON_FILE_PATH)

    def load_data(self) -> None:
        """Method to verify data format"""
        if self.data_format == 'csv':
            return self.load_csv()
        if self.data_format == 'json':
            return self.load_json()
        raise ValueError("Unsupported data format.")


def save_data(cleaned_df: pd.DataFrame, file_path: Path) -> None:
    """
    Method used to save data.
    Args:
        cleaned_df [pd.DataFrame]: Cleaned and filtered DataFrame to be saved.
        file_path [str]: file path to save data.
    """

    # Save the data frame to the data folder as pt_life_expectancy.csv
    cleaned_df.to_csv(file_path, index=False)

"""
Module to load and save data
"""

from pathlib import Path

import pandas as pd


class DataLoaderTSV:
    """
    This class is responsible to load the CSV file
    """
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def load_data(self) -> None:
        return pd.read_csv(self.file_path, sep='\t')


class DataLoaderJSON:
    """
    This class is responsible to load the JSON file
    """
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def load_data(self) -> None:
        return pd.read_json(self.file_path)


def save_data(cleaned_df: pd.DataFrame, file_path: Path) -> None:
    """
    Method used to save data.
    Args:
        cleaned_df [pd.DataFrame]: Cleaned and filtered DataFrame to be saved.
        file_path [str]: file path to save data.
    """

    # Save the data frame to the data folder as pt_life_expectancy.csv
    cleaned_df.to_csv(file_path, index=False)

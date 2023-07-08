from pathlib import Path

import pandas as pd

PARENT_PATH = Path(__file__).parent
FILE_PATH = PARENT_PATH / 'data'
TSV_FILE_NAME = 'eu_life_expectancy_raw.tsv'
JSON_FILE_NAME = 'eurostat_life_expect.json'
OUTPUT_FILE_NAME = 'pt_life_expectancy.csv'
TSV_FILE_PATH = FILE_PATH / TSV_FILE_NAME
JSON_FILE_PATH = FILE_PATH / JSON_FILE_NAME


class DataLoader:
    """
    This class is responsible for verifying the format
    and assign the right load method
    """
    def __init__(self, data_format):
        self.data_format = data_format

    def load_csv(self):
        return pd.read_csv(TSV_FILE_PATH, sep='\t')

    def load_json(self):
        return pd.read_json(JSON_FILE_PATH)

    def load_data(self):
        if self.data_format == 'csv':
            return self.load_csv()
        elif self.data_format == 'json':
            return self.load_json()
        else:
            raise ValueError("Unsupported data format.")


def save_data(clean_df: pd.DataFrame, file_path: Path) -> None:
    """
    Method used to save data.
    Args:
        clean_df [pd.DataFrame]: Cleaned and filtered DataFrame to be saved.
        file_path [str]: file path to save data.
    """

    # Save the data frame to the data folder as pt_life_expectancy.csv
    clean_df.to_csv(file_path, index=False)

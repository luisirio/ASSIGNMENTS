from pathlib import Path

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Method used to load data.

    Returns:
        [pd.DataFrame]: Dataframe to be cleaned.
    """
    data_df = pd.read_csv(file_path, sep='\t')

    return data_df

def save_data(clean_df: pd.DataFrame, file_path: Path) -> None:
    """
    Method used to save data.
    Args:
        clean_df [pd.DataFrame]: Cleaned and filtered DataFrame to be saved.
    """

    # Save the resulting data frame to the data folder as pt_life_expectancy.csv
    clean_df.to_csv(file_path, index = False)
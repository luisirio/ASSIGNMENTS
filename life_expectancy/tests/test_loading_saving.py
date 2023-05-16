"""Tests for the loading and saving module"""

from pathlib import Path
from unittest.mock import Mock

import pandas as pd

from life_expectancy.loading_saving import load_data, save_data

PARENT_PATH = Path(__file__).parent.parent
FILE_PATH = PARENT_PATH / 'data'
INPUT_FILE_NAME = 'eu_life_expectancy_raw.tsv'
OUTPUT_FILE_NAME = 'pt_life_expectancy.csv'
INPUT_FILE_PATH = FILE_PATH / INPUT_FILE_NAME
OUTPUT_FILE_PATH = FILE_PATH / OUTPUT_FILE_NAME

def test_load_data(eu_life_expectancy_raw):

    """Test load_data function"""
    data_df = load_data(INPUT_FILE_PATH)
    pd.testing.assert_frame_equal(data_df, eu_life_expectancy_raw)


def test_save_data():

    """Test save_data function"""
    # Create a mock DataFrame to use as input
    mock_df = Mock(spec=pd.DataFrame)

    # Call the save_data function with the mock DataFrame
    save_data(mock_df, OUTPUT_FILE_PATH)

    # Assert that the DataFrame was saved to the correct file
    mock_df.to_csv.assert_called_once_with(OUTPUT_FILE_PATH, index=False)
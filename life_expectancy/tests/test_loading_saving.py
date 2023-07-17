"""Tests for the loading and saving module"""

from pathlib import Path
from unittest.mock import Mock

import pandas as pd

from life_expectancy.loading_saving import (DataLoaderJSON, DataLoaderTSV,
                                            save_data)

PARENT_PATH = Path(__file__).parent.parent
FILE_PATH = PARENT_PATH / 'data'
OUTPUT_FILE_NAME = 'pt_life_expectancy.csv'
OUTPUT_FILE_PATH = FILE_PATH / OUTPUT_FILE_NAME
TSV_FILE_NAME = 'eu_life_expectancy_raw.tsv'
JSON_FILE_NAME = 'eurostat_life_expect.json'
TSV_FILE_PATH = FILE_PATH / TSV_FILE_NAME
JSON_FILE_PATH = FILE_PATH / JSON_FILE_NAME


def test_load_data_tsv(eu_life_expectancy_raw):

    """Test load_data function for csv"""
    data_df = DataLoaderTSV(TSV_FILE_PATH).load_data()
    pd.testing.assert_frame_equal(data_df, eu_life_expectancy_raw)


def test_load_data_json(eurostat_life_expect):

    """Test load_data function for json"""
    data_df = DataLoaderJSON(JSON_FILE_PATH).load_data()
    pd.testing.assert_frame_equal(data_df, eurostat_life_expect)


def test_save_data():

    """Test save_data function"""
    # Create a mock DataFrame to use as input
    mock_df = Mock(spec=pd.DataFrame)

    # Call the save_data function with the mock DataFrame
    save_data(mock_df, OUTPUT_FILE_PATH)

    # Assert that the DataFrame was saved to the correct file
    mock_df.to_csv.assert_called_once_with(OUTPUT_FILE_PATH, index=False)

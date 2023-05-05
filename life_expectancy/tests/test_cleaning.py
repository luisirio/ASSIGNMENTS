"""Tests for the cleaning module"""
from pathlib import Path
from unittest.mock import Mock

import pandas as pd

from life_expectancy.cleaning import clean_data
from life_expectancy.loading_saving import load_data, save_data
from life_expectancy.main import main

from . import OUTPUT_DIR


def test_main(pt_life_expectancy_expected):
    """Run the `main` function and compare the output to the expected output"""
    pt_life_expectancy_actual = main('PT').reset_index(drop=True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )


def test_load_data(eu_life_expectancy_raw):

    """Test load_data function"""
    data_df = load_data().reset_index(drop=True)
    pd.testing.assert_frame_equal(data_df, eu_life_expectancy_raw)


def test_clean_data(eu_life_expectancy_raw, pt_life_expectancy_expected):

    """Test clean_data function"""
    clean_df = clean_data(eu_life_expectancy_raw, 'PT').reset_index(drop = True)
    pd.testing.assert_frame_equal(clean_df, pt_life_expectancy_expected)


def test_save_data():

    """Test save_data function"""
    # Create a mock DataFrame to use as input
    mock_df = Mock(spec=pd.DataFrame)

    # Call the save_data function with the mock DataFrame
    save_data(mock_df)

    # Assert that the DataFrame was saved to the correct file
    expected_file_path = f"{Path(__file__).parent.parent}/data/pt_life_expectancy.csv"
    mock_df.to_csv.assert_called_once_with(expected_file_path, index=False)


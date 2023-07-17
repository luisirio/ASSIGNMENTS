"""Tests for the cleaning module"""

import pandas as pd

from life_expectancy.cleaning import DataCleanerJSON, DataCleanerTSV


def test_clean_data_csv(eu_life_expectancy_raw, pt_life_expectancy_expected):

    """Test clean_data function for csv"""
    cleaned_df = DataCleanerTSV().clean_data(
                eu_life_expectancy_raw, 'PT'
            ).reset_index(drop=True)
    pd.testing.assert_frame_equal(cleaned_df, pt_life_expectancy_expected)


def test_clean_data_json(eurostat_life_expect, pt_life_expectancy_expected):

    """Test clean_data function for json"""
    cleaned_df = DataCleanerJSON().clean_data(
                eurostat_life_expect, 'PT'
            ).reset_index(drop=True)
    pd.testing.assert_frame_equal(cleaned_df, pt_life_expectancy_expected)

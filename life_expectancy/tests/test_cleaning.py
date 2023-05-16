"""Tests for the cleaning module"""

import pandas as pd

from life_expectancy.cleaning import clean_data


def test_clean_data(eu_life_expectancy_raw, pt_life_expectancy_expected):

    """Test clean_data function"""
    clean_df = clean_data(eu_life_expectancy_raw, 'PT').reset_index(drop = True)
    pd.testing.assert_frame_equal(clean_df, pt_life_expectancy_expected)

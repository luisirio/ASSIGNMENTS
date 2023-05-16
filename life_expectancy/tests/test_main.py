"""Tests for the main module"""

from unittest import mock

import pandas as pd

from life_expectancy.main import main


def test_main(pt_life_expectancy_expected):
    """Run the `main` function and compare the output to the expected output"""
    with mock.patch.object(pd.DataFrame, "to_csv") as mock_to_csv:
        mock_to_csv.side_effect = print("Message: Dataframe saved to CSV")

        pt_life_expectancy_actual = main('PT').reset_index(drop=True)

        pd.testing.assert_frame_equal(
            pt_life_expectancy_actual, pt_life_expectancy_expected
        )

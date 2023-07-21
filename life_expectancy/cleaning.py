"""
Module to clean data
"""

from dataclasses import dataclass

import pandas as pd

from life_expectancy.region import Region


@dataclass
class DataCleanerTSV:
    """
    This class is responsible to clean CSV dataframe
    """

    def clean_data(self, data_df: pd.DataFrame, region: str) -> pd.DataFrame:
        """Method to verify region and clean data_df"""

        # Region defined to clean dataframe
        country = Region(region)

        # 'unit,sex,age,geo\\time'
        initial_columns = data_df.columns[0]

        # ['unit', 'sex', 'age', 'geo\\time']
        new_columns = data_df.columns[0].split(',')

        data_df[new_columns] = data_df[
                                    initial_columns
                                ].str.split(',', expand=True)

        data_df = data_df.drop(columns=initial_columns)

        cleaned_df = pd.melt(
                data_df,
                new_columns,
                var_name='year',
                value_name='value'
            )

        # rename column
        cleaned_df.rename(columns={'geo\\time': 'region'}, inplace=True)

        # Ensures year is an int
        cleaned_df['year'] = cleaned_df['year'].astype('int')

        # remove non-numeric characters and extract float values
        cleaned_df['value'] = cleaned_df['value'].str.extract(
                                    r'(\d+\.\d+)', expand=False
                                ).astype(float)

        # Filter by region
        cleaned_df = cleaned_df[cleaned_df['region'] == country.value]

        # drop NaN values
        cleaned_df = cleaned_df.dropna(subset=['value'])

        return cleaned_df


@dataclass
class DataCleanerJSON:
    """
    This class is responsible to clean JSON dataframe
    """

    def clean_data(self, data_df: pd.DataFrame, region: str) -> pd.DataFrame:
        """Method to verify region and clean data_df"""

        # Region defined to clean dataframe
        country = Region(region)

        # Drop columns that are not in the list we want
        cleaned_df = data_df.drop(columns='flag', axis=1)
        cleaned_df = cleaned_df.drop(columns='flag_detail', axis=1)

        # Rename columns
        cleaned_df = cleaned_df.rename(
                    columns={'country': 'region', 'life_expectancy': 'value'}
                )

        # Filter by region
        cleaned_df = cleaned_df[cleaned_df['region'] == country.value]

        # drop NaN values
        cleaned_df = cleaned_df.dropna(subset=['value'])

        return cleaned_df

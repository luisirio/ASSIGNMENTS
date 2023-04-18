import argparse
from pathlib import Path

import pandas as pd


def load_data() -> pd.DataFrame:
    """
    Method used to load data.

    Returns:
        [pd.DataFrame]: Dataframe to be cleaned.
    """
    data_df = pd.read_csv(
        f"{Path(__file__).parent}/data/eu_life_expectancy_raw.tsv", sep='\t')

    return data_df

def clean_data(data_df: pd.DataFrame, region: str = 'PT') -> pd.DataFrame:
    """
    Method used to clean data.
    Args:
        data_df [pd.DataFrame]: The raw dataframe.
        region [str]: Region to be selected.
    Returns:
        [pd.DataFrame]: Data cleaned and filtered by region.
    """

    # 'unit,sex,age,geo\\time'
    initial_columns = data_df.columns[0]

    # ['unit', 'sex', 'age', 'geo\\time']
    new_columns = data_df.columns[0].split(',')

    data_df[new_columns] = data_df[initial_columns].str.split(',', expand=True)

    data_df = data_df.drop(columns=initial_columns)

    clean_df = pd.melt(
            data_df,
            new_columns,
            var_name='year',
            value_name='value'
        )

    # rename column
    clean_df.rename(columns={'geo\\time':'region'}, inplace = True)

    # Ensures year is an int
    clean_df['year'] = clean_df['year'].astype('int')

    # remove non-numeric characters and extract float values
    clean_df['value'] = clean_df['value'].str.extract(r'(\d+\.\d+)', expand=False).astype(float)

    # Filters only the data where region equal to PT (Portugal)
    clean_df = clean_df[clean_df['region']== region]

    # drop NaN values
    clean_df = clean_df.dropna(subset=['value'])

    return clean_df


def save_data(clean_df: pd.DataFrame) -> None:
    """
    Method used to save data.
    Args:
        clean_df [pd.DataFrame]: Cleaned and filtered DataFrame to be saved.
    """

    # Save the resulting data frame to the data folder as pt_life_expectancy.csv
    clean_df.to_csv(
            f"{Path(__file__).parent}/data/pt_life_expectancy.csv", index = False)


def main(region: str) -> None:
    """
    Main function.
    Method that loads, cleans and saves data.
    """
    data_df = load_data()
    clean_df = clean_data(data_df, region)
    save_data(clean_df)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('region')
    args = parser.parse_args()
    main(args.region)

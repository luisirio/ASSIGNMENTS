import os
import pandas as pd
import argparse

# Comment: Only to test CI

def clean_data(region: str = 'PT'):
    """
    Method used to clean data.
    """

    raw_data = pd.read_csv(
            f"{os.getcwd()}/life_expectancy/data/eu_life_expectancy_raw.tsv", sep='\t')

    # 'unit,sex,age,geo\\time'
    initial_columns = raw_data.columns[0]

    # ['unit', 'sex', 'age', 'geo\\time']
    new_columns = raw_data.columns[0].split(',')

    raw_data[new_columns] = raw_data[initial_columns].str.split(',', expand=True)

    raw_data = raw_data.drop(columns=initial_columns)

    melted_df = pd.melt(
            raw_data,
            new_columns,
            var_name='year',
            value_name='value'
        )
    
    # rename column
    melted_df.rename(columns={'geo\\time':'region'}, inplace = True)

    # Ensures year is an int
    melted_df['year'] = melted_df['year'].astype('int')

    # remove non-numeric characters and extract float values
    melted_df['value'] = melted_df['value'].str.extract(r'(\d+\.\d+)', expand=False).astype(float)

    # Filters only the data where region equal to PT (Portugal)
    melted_df = melted_df[melted_df['region']== region]

    # drop NaN values
    melted_df = melted_df.dropna(subset=['value'])

    # Save the resulting data frame to the data folder as pt_life_expectancy.csv
    melted_df.to_csv(f"{os.getcwd()}/life_expectancy/data/pt_life_expectancy.csv", index = False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('region')
    args = parser.parse_args()
    clean_data(args.region)

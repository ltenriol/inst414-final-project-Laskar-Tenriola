import pandas as pd
import os

def load_data():
    mortgage_path = 'data/extracted/zhvi_mortgage.csv'
    rent_path = 'data/extracted/zori_rent.csv'

    mortgage = pd.read_csv(mortgage_path)
    rent = pd.read_csv(rent_path)

    return mortgage, rent

def clean_data(mortgage, rent):
    if 'SizeRank' in mortgage.columns:
        mortgage = mortgage.drop(columns=['SizeRank'])
    if 'SizeRank' in rent.columns:
        rent = rent.drop(columns=['SizeRank'])

    #remove duplicates
    mortgage = mortgage.drop_duplicates()
    rent = rent.drop_duplicates()

    #drop rows with no regionID
    if 'RegionID' in mortgage.columns:
        mortgage = mortgage.dropna(subset=['RegionID'])
    if 'RegionID' in rent.columns:
        rent = rent.dropna(subset=['RegionID'])

    #identify ID columns 
    def get_id(df):
        for idx, col in enumerate(df.columns):
            if col[:2].isdigit() and ('/' in col):
                return list(df.columns[:idx])
        return list(df.columns)

    mortgage_id = get_id(mortgage)
    rent_id = get_id(rent)

    #pivot on date columns
    mortgage_long = pd.melt(
        mortgage,
        id_vars=mortgage_id,
        var_name='Month',
        value_name='Mortgage'
    )
    rent_long = pd.melt(
        rent,
        id_vars=rent_id,
        var_name='Month',
        value_name='Rent'
    )

    #merge datasets
    merge_cols = [c for c in ['RegionID', 'Region', 'State', 'City', 'Month'] if c in mortgage_long.columns and c in rent_long.columns]
    merged = pd.merge(mortgage_long, rent_long, on=merge_cols, how='inner')

    #save the cleaned data
    os.makedirs('data/processed', exist_ok=True)
    merged.to_csv('data/processed/cleaned_housing_data.csv', index=False)

    print("Data cleaning and wrangling complete. Saved to data/processed/cleaned_housing_data.csv")
    return merged

if __name__ == "__main__":
    mortgage, rent = load_data()
    clean_data(mortgage, rent)

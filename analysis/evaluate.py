import pandas as pd
import os

def cost_comparison():
    home = pd.read_csv('data/outputs/home_value_forecast.csv')
    rent = pd.read_csv('data/outputs/rent_value_forecast.csv')

    #cost per region
    home_total = home.groupby('RegionID')['Mortgage'].sum().reset_index().rename(columns={'Mortgage': 'FiveYearHomeCost'})
    rent_total = rent.groupby('RegionID')['Rent'].sum().reset_index().rename(columns={'Rent': 'FiveYearRentCost'})


    #decide which is better
    results = pd.merge(home_total, rent_total, on='RegionID', how='outer') 

    results['BetterOption'] = results.apply(lambda row: 'Buy' if row['FiveYearHomeCost'] < row['FiveYearRentCost'] else 'Rent', axis=1)

    os.makedirs('data/outputs', exist_ok=True)
    results.to_csv('data/outputs/buy_vs_rent_results.csv', index=False)

if __name__ == "__main__":
    cost_comparison()


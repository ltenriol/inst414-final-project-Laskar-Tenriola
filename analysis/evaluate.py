import pandas as pd
import numpy as np
import os

def cost_comparison():
    home = pd.read_csv('data/outputs/home_value_forecast.csv')
    rent = pd.read_csv('data/outputs/rent_value_forecast.csv')

    # Sum 5-year totals per region
    home_total = (home
                  .groupby('RegionID', as_index=False)['Mortgage']
                  .sum()
                  .rename(columns={'Mortgage': 'FiveYearHomeCost'}))

    rent_total = (rent
                  .groupby('RegionID', as_index=False)['Rent']
                  .sum()
                  .rename(columns={'Rent': 'FiveYearRentCost'}))

    # Join on regions present in both (use 'outer' if you want to keep unmatched and then fill)
    results = pd.merge(home_total, rent_total, on='RegionID', how='inner')

    # fill null
    results[['FiveYearHomeCost','FiveYearRentCost']] = results[['FiveYearHomeCost','FiveYearRentCost']].fillna(np.inf)

    results['BetterOption'] = np.where(
        results['FiveYearHomeCost'] < results['FiveYearRentCost'],
        'Buy',
        'Rent'
    )

    os.makedirs('data/outputs', exist_ok=True)
    results.to_csv('data/outputs/buy_vs_rent_results.csv', index=False)

if __name__ == "__main__":
    cost_comparison()

















# import pandas as pd
# import os

# def cost_comparison():
#     home = pd.read_csv('data/outputs/home_value_forecast.csv')
#     rent = pd.read_csv('data/outputs/rent_value_forecast.csv')

#     #cost per region
#     home_total = home.groupby('RegionID')['Mortgage'].sum().reset_index().rename(columns={'Mortgage': 'FiveYearHomeCost'})
#     rent_total = rent.groupby('RegionID')['Rent'].sum().reset_index().rename(columns={'Rent': 'FiveYearRentCost'})


#     #decide which is better
#     results = pd.merge(home_total, rent_total, on='RegionID', how='outer') 

#     results['BetterOption'] = results.apply(lambda row: 'Buy' if row['FiveYearHomeCost'] < row['FiveYearRentCost'] else 'Rent', axis=1)

#     os.makedirs('data/outputs', exist_ok=True)
#     results.to_csv('data/outputs/buy_vs_rent_results.csv', index=False)

# if __name__ == "__main__":
#     cost_comparison()


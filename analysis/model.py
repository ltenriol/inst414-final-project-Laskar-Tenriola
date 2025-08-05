import pandas as pd
import numpy as np
import os

#linear regression for forecasting home and rent values
def forecast(df, value_col, forecast_months=60):
    forecasts = []
    for key, group in df.groupby('RegionID'):
        group = group.sort_values('Month')
        months_numeric = np.arange(len(group))
        values = group[value_col].values

        #check to see if there is enough data
        if len(values) > 12:
            coeffs = np.polyfit(months_numeric, values, 1)
            last_month = months_numeric[-1]
            forecast_months_numeric = np.arange(last_month + 1, last_month + forecast_months + 1)
            forecast_values = np.polyval(coeffs, forecast_months_numeric)
            for i, fv in enumerate(forecast_values):
                forecasts.append({
                    'RegionID': key,
                    'Month': f'forecast_{i+1}',
                    value_col: fv
                })
    return pd.DataFrame(forecasts)

def run_forecast():
    data_path = 'data/processed/cleaned_housing_data.csv'
    df = pd.read_csv(data_path)

    #forecast home values and rent values 
    home_forecast = forecast(df, value_col='Mortgage', forecast_months=60)
    rent_forecast = forecast(df, value_col='Rent', forecast_months=60)
    os.makedirs('data/outputs', exist_ok=True)
    home_forecast.to_csv('data/outputs/home_value_forecast.csv', index=False)
    rent_forecast.to_csv('data/outputs/rent_value_forecast.csv', index=False)
    print("Forecasts saved to data/outputs/")

if __name__ == "__main__":
    run_forecast()

import pandas as pd
import numpy as np
import os

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def forecast(df, value_col, forecast_months=60, degree=1, min_obs=12):
    forecasts = []

    # ensure month is a datetime column
    df = df.copy()
    df['Month'] = pd.to_datetime(df['Month'], errors='coerce')

    # clean each region data
    for region_id, group in df.groupby('RegionID'):
        g = group[['Month', value_col]].dropna()
        g = g[g['Month'].notna()].sort_values('Month').reset_index(drop=True)

        # check to see if there is enough data
        if len(g) < min_obs:
            continue

        # creating time index from the months
        X = np.arange(len(g)).reshape(-1, 1)
        y = g[value_col].values

        # fit polynomial regression model
        model = make_pipeline(
            PolynomialFeatures(degree=degree, include_bias=False),
            LinearRegression()
        )
        model.fit(X, y)

        # future predictions and creation of future month stamps
        future= np.arange(len(g), len(g) + forecast_months).reshape(-1, 1)
        y_prediction = model.predict(future)

        # build month stamps 
        start_month = g['Month'].iloc[-1] + pd.offsets.MonthBegin(1)
        future_months = pd.date_range(start=start_month, periods=forecast_months, freq='MS')

        # append the forecast results
        forecasts.extend(
            {
                'RegionID': region_id,
                'Month': m,              
                value_col: float(v)      
            }
            for m, v in zip(future_months, y_prediction)
        )

    return pd.DataFrame(forecasts)

def run_forecast():
    data_path = 'data/processed/cleaned_housing_data.csv'
    df = pd.read_csv(data_path)

    # forecast home values and rent values 
    home_forecast = forecast(df, value_col='Mortgage', forecast_months=60, degree=1)
    rent_forecast = forecast(df, value_col='Rent', forecast_months=60, degree=1)

    os.makedirs('data/outputs', exist_ok=True)
    home_forecast.to_csv('data/outputs/home_value_forecast.csv', index=False)
    rent_forecast.to_csv('data/outputs/rent_value_forecast.csv', index=False)
    print("Forecasts saved to data/outputs/")

if __name__ == "__main__":
    run_forecast()




































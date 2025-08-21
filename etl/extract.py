import pandas as pd
import os

def extract_data():
    mortgage_url = 'https://files.zillowstatic.com/research/public_csvs/total_monthly_payment/Metro_total_monthly_payment_downpayment_0.20_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv?t=1755719502'
    rent_url = 'https://files.zillowstatic.com/research/public_csvs/zori/Metro_zori_uc_sfrcondomfr_sm_month.csv?t=1755719502'
    
    # download csv files and put into data folder
    mortgage_file = pd.read_csv(mortgage_url)
    rent_file = pd.read_csv(rent_url)
    os.makedirs('data/extracted', exist_ok=True)

    # save the data to the extracted folder
    mortgage_path = 'data/extracted/zhvi_mortgage.csv'
    rent_path = 'data/extracted/zori_rent.csv'
    mortgage_file.to_csv(mortgage_path, index=False)
    rent_file.to_csv(rent_path, index=False)

    # return the path of extracted data
    extracted_data = [mortgage_path, rent_path]
    return extracted_data

extract_data()

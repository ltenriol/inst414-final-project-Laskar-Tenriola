import pandas as pd
import os

def extract_data():
    extacted_data = [
        'data/extracted/zhvi_mortgage.csv',
        'data/extracted/zori_rent.csv'
    ]
    
    data = {}
    
    for file in extacted_data:
        if os.path.exists(file):
            df = pd.read_csv(file)
            data[file] = df
            print(df.head(), "\n")
        else:
            print(f"error: file not found")
    
    return data
    
extract_data()


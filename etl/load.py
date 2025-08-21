from etl.transform import clean_data, load_data
import os

def main():
    #read inputs
    mortgage, rent = load_data()
    merged = clean_data(mortgage, rent)

    #load 
    os.makedirs('data/processed', exist_ok=True)
    out_path = 'data/processed/cleaned_housing_data.csv'
    merged.to_csv(out_path, index=False)

if __name__ == "__main__":
    main()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_cost_comparison():
    data_path = 'data/outputs/buy_vs_rent_results.csv'

    df = pd.read_csv(data_path)
    
    df_plot = df.head(20)

    plt.figure(figsize=(12, 6))
    bar_width = 0.4
    x = range(len(df_plot))

    plt.bar(x, df_plot['FiveYearHomeCost'], width=bar_width, label='Buy (5 yr)', alpha=0.7)
    plt.bar([p + bar_width for p in x], df_plot['FiveYearRentCost'], width=bar_width, label='Rent (5 yr)', alpha=0.7)
    plt.xlabel('RegionID')
    plt.ylabel('Total 5 Year Cost')
    plt.title('5-Year Cost: Buying vs. Renting')
    plt.xticks([p + bar_width/2 for p in x], df_plot['RegionID'], rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_better_option_counts():
    data_path = 'data/outputs/buy_vs_rent_results.csv'

    df = pd.read_csv(data_path)
    sns.countplot(x='BetterOption', data=df)
    plt.title('Number of Regions Where Buying or Renting is Better')
    plt.ylabel('Number of Regions')
    plt.xlabel('Better Option')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_cost_comparison()
    plot_better_option_counts()

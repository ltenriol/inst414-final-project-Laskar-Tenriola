# Predicting the Financial Effectiveness of Buying vs. Renting in the United States

## Project Overview

The business problem for this project: Is it financially better to buy or rent a home in the United States over the next 5 years?

- **Business Problem:**  
  Many individuals and real estate professionals debate whether buying or renting is more effective financially, especially within the current housing market. This project aims to provide an answer by forecasting and comparing costs of over 5 years for both options in different US regions.
- **Datasets Used:**  
  - [Zillow Home Value Index (ZHVI)](https://www.zillow.com/research/data/)
  - [Zillow Observed Rent Index (ZORI)](https://www.zillow.com/research/data/)
- **Techniques Employed:**  
  - Data cleaning and transformation 
  - Time series forecasting
  - Cost simulation analysis
  - Visualization with Matplotlib and Seaborn
- **Expected Outputs:**  
  - CSV files comparing the costs over 5 years of buying vs. renting by region
  - Bar charts and summary graphs of the results


## Setup Instructions

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/ltenriol/inst414-final-project-Laskar-Tenriola.git
    cd inst414-final-project-Laskar-Tenriola
    ```

2. **Create and Activate a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install Required Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    Or install manually:
    ```bash
    pip install pandas matplotlib seaborn
    ```

---

## Running the Project

Run each stage of the pipeline in order from the project root directory:

1. **ETL - Extract:**  
    ```bash
    python etl/extract.py
    ```
2. **ETL - Transform:**  
    ```bash
    python etl/transform.py
    ```
3. **ETL - Load:**  
    ```bash
    python etl/load.py
    ```
4. **Analysis:**  
    ```bash
    python analysis/model.py
    python analysis/evaluate.py
    ```
5. **Visualization:**  
    ```bash
    python vis/visualizations.py
    ```

Or, run the full pipeline (if `main.py` is set up for that):
```bash
python main.py

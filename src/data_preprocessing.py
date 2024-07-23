import pandas as pd
import os

def preprocess_data(input_path, output_path):
    data = pd.read_csv(input_path)
    # Perform data cleaning and preprocessing
    master_table = data # For simplicity, assume it's processed
    master_table.to_csv(output_path, index=False)

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'customer_data.csv')
    preprocess_data(file_path, '../data/processed/master_table.csv')

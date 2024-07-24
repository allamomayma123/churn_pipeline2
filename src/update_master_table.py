import os
import pandas as pd

def update_master_table(new_data_path, master_table_path):
    new_data_path = os.path.abspath(new_data_path)
    master_table_path = os.path.abspath(master_table_path)
    
    if not os.path.exists(new_data_path):
        raise FileNotFoundError(f"The file {new_data_path} does not exist.")
    
    new_data = pd.read_csv(new_data_path)
    # Continue with your logic to update the master table

if __name__ == "__main__":
    update_master_table('/home/vsts/work/1/s/data/raw/new_data.csv', '/home/vsts/work/1/s/data/processed/master_table.csv')

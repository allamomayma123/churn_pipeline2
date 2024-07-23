import pandas as pd

def update_master_table(new_data_path, master_table_path):
    new_data = pd.read_csv(new_data_path)
    master_table = pd.read_csv(master_table_path)
    updated_master_table = pd.concat([master_table, new_data])
    updated_master_table.to_csv(master_table_path, index=False)

if __name__ == "__main__":
    update_master_table('../data/raw/new_data.csv', '../data/processed/master_table.csv')

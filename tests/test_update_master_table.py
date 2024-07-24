import os
import sys
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from update_master_table import update_master_table

def test_update_master_table(tmp_path):
    # Create sample input CSVs
    new_data_csv = tmp_path / "new_data.csv"
    new_data = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})
    new_data.to_csv(new_data_csv, index=False)

    master_table_csv = tmp_path / "master_table.csv"
    master_table = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    master_table.to_csv(master_table_csv, index=False)

    # Run the update master table function
    update_master_table(new_data_csv, master_table_csv)

    # Check contents of the updated master table
    updated_master_table = pd.read_csv(master_table_csv)
    expected_data = pd.concat([master_table, new_data], ignore_index=True)
    pd.testing.assert_frame_equal(updated_master_table, expected_data)

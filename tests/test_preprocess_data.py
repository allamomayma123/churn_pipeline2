import os
import pandas as pd
from src.data_preprocessing import preprocess_data

def test_preprocess_data(tmp_path):
    # Create a sample input CSV
    input_csv = tmp_path / "input.csv"
    data = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    data.to_csv(input_csv, index=False)

    # Output path
    output_csv = tmp_path / "output.csv"

    # Run the preprocessing function
    preprocess_data(input_csv, output_csv)

    # Check if output CSV is created
    assert os.path.exists(output_csv)

    # Check contents of the output CSV
    output_data = pd.read_csv(output_csv)
    pd.testing.assert_frame_equal(data, output_data)

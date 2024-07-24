import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from train_model import train_model

def test_train_model(monkeypatch, tmp_path):
    def mock_start_run():
        class MockRun:
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc_value, traceback):
                pass

        return MockRun()

    monkeypatch.setattr("mlflow.start_run", mock_start_run)

    # Create a sample input CSV
    input_csv = tmp_path / "input.csv"
    data = pd.DataFrame({
        'feature1': [1, 2],
        'feature2': [3, 4],
        'churn': [0, 1]
    })
    data.to_csv(input_csv, index=False)

    # Run the train model function
    train_model(input_csv)

import os
import pandas as pd
from src.score_model import score_model

def test_score_model(monkeypatch, tmp_path):
    def mock_load_model(model_uri):
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier()
        model.fit([[0]], [0])  # Dummy fit
        return model

    monkeypatch.setattr("mlflow.sklearn.load_model", mock_load_model)

    # Create a sample input CSV
    input_csv = tmp_path / "input.csv"
    data = pd.DataFrame({'feature': [1]})
    data.to_csv(input_csv, index=False)

    # Output path
    output_csv = tmp_path / "predictions.csv"

    # Run the scoring function
    score_model(input_csv)

    # Check if output CSV is created
    assert os.path.exists('data/processed/predictions.csv')

    # Check contents of the output CSV
    predictions = pd.read_csv('data/processed/predictions.csv')
    assert 'predictions' in predictions.columns

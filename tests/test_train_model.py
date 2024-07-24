import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pytest

def train_model(data_path):
    """
    Cette fonction fait l'entrainement du modele.
    """
    data = pd.read_csv(data_path)
    X = data.drop('churn', axis=1)
    y = data['churn']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run() as run:
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        # Log model and metrics to MLflow
        mlflow.log_metric('accuracy', accuracy)
        mlflow.sklearn.log_model(model, "model")

        print(f"Model logged in run {run.info.run_id}")

def test_train_model(monkeypatch, tmp_path):
    def mock_start_run():
        class MockRun:
            def __enter__(self):
                # Mock the info attribute
                class MockInfo:
                    def __init__(self):
                        self.run_id = "mock_run_id"
                
                self.info = MockInfo()
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

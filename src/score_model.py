import mlflow
import pandas as pd
from mlflow.tracking import MlflowClient

def score_model(data_path):
    data = pd.read_csv(data_path)
    client = MlflowClient()
    model = mlflow.sklearn.load_model(f"models:/ChurnModel/Production")
    predictions = model.predict(data)
    # Save predictions
    pd.DataFrame(predictions, columns=['predictions']).to_csv('data/processed/predictions.csv', index=False)

if __name__ == "__main__":
    score_model('data/processed/new_data.csv')

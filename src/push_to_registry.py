import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier

# Set the tracking URI to the MLflow server
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("churn_prediction")

# Load the model saved in the previous step
model_path = 'model_training/model.pkl'
model = mlflow.sklearn.load_model(model_path)

# Log model to MLflow
with mlflow.start_run() as run:
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_param("model_type", "RandomForest")
    # Here, you can use a placeholder accuracy value or re-evaluate the model if needed
    mlflow.log_metric("accuracy", 0.85)  # Replace with actual accuracy if available

print(f"Model logged in run {run.info.run_id}")

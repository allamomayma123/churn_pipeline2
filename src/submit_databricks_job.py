import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def submit_databricks_job():
    """
    Cette fonction fait quelque chose d'important.
    """
    url = "https://adb-3733434531606738.18.azuredatabricks.net/api/2.1/jobs/runs/submit"
    headers = {
        "Authorization": f"Bearer {os.getenv('DATABRICKS_TOKEN')}",
        "Content-Type": "application/json"
    }
    payload = {
        "run_name": "EDA job",
        "existing_cluster_id": os.getenv('CLUSTER_ID'),
        "notebook_task": {
            "notebook_path": "/Workspace/Repos/omayma.allam@artefact.com/churn-databricks/DATA_PREPARATION"
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.json())

if __name__ == "__main__":
    submit_databricks_job()

import requests
from src.submit_databricks_job import submit_databricks_job

def test_submit_databricks_job(monkeypatch):
    class MockResponse:
        def json(self):
            return {"result": "success"}

    def mock_post(url, headers, json, timeout):
        return MockResponse()

    monkeypatch.setattr(requests, "post", mock_post)

    # Run the submit job function
    result = submit_databricks_job()

    # Check the result
    assert result['result'] == 'success'

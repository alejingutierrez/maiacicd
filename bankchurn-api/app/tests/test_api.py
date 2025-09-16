import numpy as np
import pandas as pd
from fastapi.testclient import TestClient


def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    # Given
    payload = {
        # ensure pydantic plays well with np.nan
        "inputs": test_data.replace({np.nan: None}).to_dict(orient="records")
    }

    # When
    response = client.post(
        "/api/v1/predict",
        json=payload,
    )

    # Then
    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data["predictions"]
    assert prediction_data["errors"] is None
    # Check that we get a valid prediction (0 or 1 for churn prediction)
    assert prediction_data["predictions"][0] in [0, 1]


def test_health_endpoint(client: TestClient) -> None:
    # When
    response = client.get("/api/v1/health")
    
    # Then
    assert response.status_code == 200
    health_data = response.json()
    assert "name" in health_data
    assert "api_version" in health_data
    assert "model_version" in health_data

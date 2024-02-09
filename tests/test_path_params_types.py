from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_path_params_types():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}

def test_path_params_types_str():
    response = client.get("/items/foo")
    assert response.status_code == 422

def test_path_params_types_float():
    response = client.get("/items/4.2")
    assert response.status_code == 422

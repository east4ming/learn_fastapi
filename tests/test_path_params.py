from fastapi.testclient import TestClient
from src.main import app, ModelName

client = TestClient(app)

# Types
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

# Order
def test_read_user_me():
    response = client.get("/users/me")
    assert response.json() == {"users_me": "the current user"}

def test_read_user():
    user_id = "foo"
    response = client.get("/users/foo")
    assert response.json() == {"user_id": user_id}

# Enum
def test_get_model_alexnet():
    model_name = ModelName.alexnet.value
    response = client.get(f"/models/{model_name}")
    assert response.json() == {"model_name": model_name, "message": "Deep Learning FTW!"}

def test_get_model_lenet():
    model_name = ModelName.lenet.value
    response = client.get(f"/models/{model_name}")
    assert response.json() == {"model_name": model_name, "message": "LeCNN all the images"}

def test_get_model_other():
    model_name = "other_model"
    response = client.get(f"/models/{model_name}")
    assert response.status_code == 422

# Path
def test_params_path():
    file_path = "/home/johndoe/myfile.txt"
    response = client.get(f"/files/{file_path}")
    assert response.json() == {"file_path": file_path}

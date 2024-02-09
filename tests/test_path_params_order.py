from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# 测试 read_user_me 函数
def test_read_user_me():
    response = client.get("/users/me")
    assert response.json() == {"users_me": "the current user"}

# 测试 read_user 函数
def test_read_user():
    user_id = "foo"
    response = client.get("/users/foo")
    assert response.json() == {"user_id": user_id}

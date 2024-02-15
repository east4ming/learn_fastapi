import pytest

from fastapi.testclient import TestClient
from src.main import app, Item

client = TestClient(app)

@pytest.fixture
def test_item():
    return Item(name="Foo", price=45.2)
# 测试用例
def test_create_item(test_item):
    test_item.description="An optional description"
    
    result = client.post("/items/", json=test_item.model_dump())
    assert result.json() == test_item.model_dump()


def test_create_item_without_default_values(test_item):
    result = client.post("/items/", json=test_item.model_dump())
    assert result.json() == test_item.model_dump()

def test_create_item_with_tax(test_item):
    test_item.tax = 3.2
    result = client.post("/items/", json=test_item.model_dump())
    # 验证结果是否包含正确的字段
    assert "price_with_tax" in result.json()
    # 验证 price_with_tax 是否正确计算
    assert result.json()["price_with_tax"] == test_item.price + test_item.tax

def test_update_item_without_query(test_item):
    item_id = 1
    result = client.put(f"/items/{item_id}", json=test_item.model_dump())
    assert result.json() == {"item_id": item_id, "name": "Foo", "price": 45.2, "description": None, "tax": None}

# 测试带额外查询参数的情况
def test_update_item_with_query(test_item):
    item_id = 1
    query = "some query"
    result = client.put(f"/items/{item_id}?q={query}", json=test_item.model_dump())
    assert result.json() == {"item_id": item_id, "name": "Foo", "price": 45.2, "q": query, "description": None, "tax": None}

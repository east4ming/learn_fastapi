from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# Defaults
def test_default_query_params():
    response1 = client.get("/items/")
    response2 = client.get("/items/?skip=0&limit=10")
    assert response1.json() == response2.json()

# 测试用例1: 测试不带额外参数的read_item函数
def test_read_item_without_q():
    item_id = "foo"
    needy = "someone"
    short = True
    response = client.get(f"/items/{item_id}?needy={needy}&short={short}")
    assert response.json() == {"item_id": item_id, "needy": needy}

# 测试用例2: 测试带额外参数q的read_item函数
def test_read_item_with_q():
    item_id = "foo"
    needy = "someone"
    q = "question"
    short = True
    response = client.get(f"/items/{item_id}?needy={needy}&q={q}&short={short}")
    assert response.json() == {"item_id": item_id, "needy": needy, "q": q}

# 测试用例3: 测试short为True时的read_item函数
def test_read_item_short():
    item_id = "foo"
    needy = "someone"
    short = True
    response = client.get(f"/items/{item_id}?needy={needy}&short={short}")
    assert response.json() == {"item_id": item_id, "needy": needy}

# 测试用例4: 测试short为False时的read_item函数
def test_read_item_full():
    item_id = "foo"
    needy = "someone"
    response = client.get(f"/items/{item_id}?needy={needy}")
    assert response.json() == {"item_id": item_id, "needy": needy, "description": "This is an amazing item that has a long description."}

def test_read_item_short_type_conversion():
    item_id = "foo"
    needy = "someone"
    shorts = (False, "false", "0", "off", "no")
    for short in shorts:
        response = client.get(f"/items/{item_id}?needy={needy}&short={short}")
        assert response.json()["description"] == "This is an amazing item that has a long description."

# 测试用例1: 不包含额外参数，返回包含基本信息的字典
def test_read_user_item_without_params():
    user_id = 1
    item_id = "foo"
    result = client.get(f"/users/{user_id}/items/{item_id}")
    assert result.json() == {"item_id": item_id, "owner_id": user_id, "description": "This is an amazing item that has a long description"}

# 测试用例2: 包含额外参数，返回包含额外参数的字典
def test_read_user_item_with_q():
    user_id = 1
    item_id = "123"
    q = "test query"
    result = client.get(f"/users/{user_id}/items/{item_id}?q={q}")
    assert result.json() == {"item_id": item_id, "owner_id": user_id, "q": q, "description": "This is an amazing item that has a long description"}

# 测试用例3: 包含额外参数和short为True，返回包含基本信息和q的字典
def test_read_user_item_with_q_and_short():
    user_id = 1
    item_id = "123"
    q = "test query"
    short = True
    result = client.get(f"/users/{user_id}/items/{item_id}?q={q}&short={short}")
    assert result.json() == {"item_id": item_id, "owner_id": user_id, "q": q}

# 测试用例4: 包含额外参数和short为False，返回包含基本信息、q和description的字典
def test_read_user_item_with_q_and_not_short():
    user_id = 1
    item_id = "123"
    q = "test query"
    short = False
    result = client.get(f"/users/{user_id}/items/{item_id}?q={q}&short={short}")
    assert result.json() == {
        "item_id": item_id,
        "owner_id": user_id,
        "q": q,
        "description": "This is an amazing item that has a long description"
    }

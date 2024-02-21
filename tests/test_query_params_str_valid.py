from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_item_with_q_str_valid_min_length():
    item_id = "foo"
    needy = "someone"
    q = "q"
    short = True
    response = client.get(f"/items/{item_id}?needy={needy}&q={q}&short={short}")
    assert response.status_code == 422


def test_read_item_with_q_str_valid_max_length():
    item_id = "foo"
    needy = "someone"
    q = "longlonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglong"
    short = True
    response = client.get(f"/items/{item_id}?needy={needy}&q={q}&short={short}")
    assert response.status_code == 422


def test_read_item_with_q_str_valid_wrong_pattern():
    item_id = "foo"
    needy = "someone"
    q = "errorqxrey"
    short = True
    response = client.get(f"/items/{item_id}?needy={needy}&q={q}&short={short}")
    assert response.status_code == 422


def test_read_item_with_q_str_valid_pattern():
    item_id = "foo"
    needy = "someone"
    q = "rightquery"
    short = True
    response = client.get(f"/items/{item_id}?needy={needy}&q={q}&short={short}")
    assert response.status_code == 200

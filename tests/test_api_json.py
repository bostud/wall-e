import math

from fastapi.testclient import TestClient
from start_app import app

client = TestClient(app)

test_item_1 = {
    'name': 'Leopard',
    'items_count': 2023,
}
test_item_2 = {
    'name': 'F-16',
    'items_count': 2023,
    'description': 'Sky'
}
test_item_invalid = {
    'description': 'no name item'
}

test_item_invalid_2 = {
    'name': 'Invalid Name',
    'items_count': math.pow(2, 32),
}

json_api_base = '/api/json/items'
created_in_tests = []


def test_get_item():
    resp = client.post(json_api_base, json=test_item_1)
    assert resp.status_code == 200

    item_id = resp.json()['item_id']
    created_in_tests.append(item_id)

    resp = client.get(json_api_base + '/' + str(item_id) + '/')
    assert resp.status_code == 200

    data = resp.json()
    assert test_item_1['name'] == data['name']
    assert test_item_1['items_count'] == data['items_count']


def test_get_items():
    created_item_ids = []
    # create item 1
    resp_1 = client.post(json_api_base, json=test_item_1)
    assert resp_1.status_code == 200
    created_item_ids.append(resp_1.json()['item_id'])

    # create item 2
    resp_2 = client.post(json_api_base, json=test_item_2)
    assert resp_2.status_code == 200
    created_item_ids.append(resp_2.json()['item_id'])

    resp = client.get(json_api_base, params={'page': 1, 'limit': 25})
    assert resp.status_code == 200

    data = resp.json()
    items_ids = [i['item_id'] for i in data]
    for created_item_id in created_item_ids:
        assert created_item_id in items_ids

    created_in_tests.extend(created_item_ids)


def test_create_invalid():
    resp = client.post(json_api_base, json=test_item_invalid)
    assert resp.status_code == 422

    resp = client.post(json_api_base, json=test_item_invalid_2)
    assert resp.status_code == 422


def test_update_item():
    resp = client.post(json_api_base, json=test_item_1)
    assert resp.status_code == 200

    item_data = resp.json()
    item_id = item_data['item_id']
    created_in_tests.append(item_id)
    item_data['description'] = 'ground'

    resp = client.put(json_api_base + '/' + str(item_id) + '/', json=item_data)
    assert resp.status_code == 200

    updated_data = resp.json()
    assert updated_data['description'] == item_data['description']


def test_delete_item():
    resp = client.post(json_api_base, json=test_item_2)
    assert resp.status_code == 200

    item_data = resp.json()
    item_id = item_data['item_id']

    created_in_tests.append(item_id)

    for item_id in created_in_tests:
        resp = client.delete(json_api_base + '/' + str(item_id) + '/')
        assert resp.status_code == 200
        assert resp.json()['message'] == 'OK'

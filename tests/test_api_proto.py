
from fastapi.testclient import TestClient
from start_app import app
from api.pb_scheme import scheme_pb2

client = TestClient(app)

test_item_1 = scheme_pb2.CreateItem()
test_item_1.name = 'Leopard'
test_item_1.items_count = 2023


test_item_2 = scheme_pb2.UpdateItem()
test_item_2.name = 'F-16'
test_item_2.items_count = 2023
test_item_2.description = 'sky'

test_item_invalid = scheme_pb2.CreateItem()
test_item_invalid.name = 'F-16' * 20
test_item_invalid.description = 'sky' * 100


proto_api_base = '/api/proto/items'
created_in_tests = []


def test_get_item():
    resp = client.post(
        proto_api_base,
        content=test_item_1.SerializeToString(),
    )
    assert resp.status_code == 200
    assert resp.content

    item = scheme_pb2.Item()
    item.ParseFromString(resp.content)

    assert test_item_1.name == item.name
    assert test_item_1.items_count == item.items_count

    created_in_tests.append(item.item_id)


def test_get_items():
    created_item_ids = []

    # create item 1
    resp_1 = client.post(
        proto_api_base,
        content=test_item_1.SerializeToString(),
    )
    assert resp_1.status_code == 200
    item_1 = scheme_pb2.Item()
    item_1.ParseFromString(resp_1.content)
    created_item_ids.append(item_1.item_id)

    # create item 2
    resp_2 = client.post(
        proto_api_base,
        content=test_item_2.SerializeToString(),
    )
    assert resp_2.status_code == 200
    item_2 = scheme_pb2.Item()
    item_2.ParseFromString(resp_2.content)
    created_item_ids.append(item_2.item_id)

    resp = client.get(proto_api_base, params={'page': 1, 'limit': 25})
    assert resp.status_code == 200

    items = scheme_pb2.Items()
    items.ParseFromString(resp.content)
    items_ids = [i.item_id for i in items.items]
    for created_item_id in created_item_ids:
        assert created_item_id in items_ids

    created_in_tests.extend(created_item_ids)


def test_create_invalid():
    resp = client.post(
        proto_api_base,
        content=test_item_invalid.SerializeToString(),
    )
    assert resp.status_code == 400


def test_update_item():
    resp = client.post(
        proto_api_base,
        content=test_item_1.SerializeToString(),
    )
    assert resp.status_code == 200

    item = scheme_pb2.Item()
    item.ParseFromString(resp.content)
    created_in_tests.append(item.item_id)

    item.description = 'ground'

    resp = client.put(
        proto_api_base + '/' + str(item.item_id) + '/',
        content=item.SerializeToString(),
    )
    assert resp.status_code == 200

    updated_item = scheme_pb2.Item()
    updated_item.ParseFromString(resp.content)
    assert updated_item.description == item.description


def test_delete_item():
    for item_id in created_in_tests:
        resp = client.delete(proto_api_base + '/' + str(item_id) + '/')
        assert resp.status_code == 200

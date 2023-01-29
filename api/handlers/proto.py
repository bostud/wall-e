from typing import Optional

from fastapi import APIRouter, Response, Request, status, HTTPException, UploadFile

from api.handlers.utils import prepare_item_proto
from api.validation import is_valid_crete_proto_input
from config import RECORDS_LIMIT, BASE_PAGE
from core.controllers import (
    get_items as bl_get_items,
    create_item as bl_create_item,
    update_item as bl_update_item,
    delete_item as bl_delete_item,
)
from api.pb_scheme import scheme_pb2


class ProtoResponse(Response):
    media_type = 'application/protobuf'


proto_router = APIRouter(
    prefix='/proto',
    tags=['proto'],
    default_response_class=ProtoResponse,
)


@proto_router.get('/items/{item_id}/')
async def get_item(item_id: int) -> Optional[bytes]:
    data = bl_get_items.get_item(item_id)
    if not data:
        return None
    return prepare_item_proto(data).SerializeToString()


@proto_router.get('/items/')
async def get_items(
    limit: int = RECORDS_LIMIT,
    page: int = BASE_PAGE,
):
    data = [
        prepare_item_proto(item_data)
        for item_data in bl_get_items.get_items(limit, page)
    ]
    items = scheme_pb2.Items()
    items.items.extend(data)
    return ProtoResponse(
        content=items.SerializeToString(),
    )


@proto_router.post('/items/')
async def create_item(request: Request):
    item = await request.body()
    if not item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    _pb_item = scheme_pb2.CreateItem()
    _pb_item.ParseFromString(item)
    if not is_valid_crete_proto_input(_pb_item):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid data',
        )

    _item = bl_create_item.create_item(
        author_ip=request.client.host,
        name=_pb_item.name,
        description=_pb_item.description,
        count=_pb_item.items_count,
    )
    return ProtoResponse(
        content=prepare_item_proto(_item).SerializeToString()
    )


@proto_router.put('/items/{item_id}/')
async def update_item(request: Request, item_id: int):
    item = await request.body()
    if not item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    _pb_item = scheme_pb2.UpdateItem()
    _pb_item.ParseFromString(item)

    if not is_valid_crete_proto_input(_pb_item):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid data',
        )
    _item = bl_update_item.update_item(
        item_id,
        name=_pb_item.name,
        description=_pb_item.description,
        count=_pb_item.items_count,
    )
    return ProtoResponse(
        content=prepare_item_proto(_item).SerializeToString(),
    )


@proto_router.delete('/items/{item_id}/')
async def delete_item(item_id: int) -> Response:
    _is_deleted = bl_delete_item.delete_item(item_id)
    message = 'OK' if _is_deleted else 'Item: %s - Not found' % item_id
    return ProtoResponse(
        status_code=status.HTTP_200_OK,
        content=message,
    )

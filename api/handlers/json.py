from typing import Optional, List

from fastapi import APIRouter, Response, Request, status
from fastapi.responses import JSONResponse

from api.handlers.utils import prepare_item_response
from api.json_scheme.scheme import CreateItem, UpdateItem, Item
from config import RECORDS_LIMIT, BASE_PAGE
from core.controllers import (
    get_items as bl_get_items,
    create_item as bl_create_item,
    update_item as bl_update_item,
    delete_item as bl_delete_item,
)

json_router = APIRouter(
    prefix='/json',
    tags=['json'],
    default_response_class=JSONResponse,
)


@json_router.get('/items/{item_id}/')
async def get_item(item_id: int) -> Optional[Item]:
    data = bl_get_items.get_item(item_id)
    if not data:
        return None
    return prepare_item_response(data)


@json_router.get('/items/')
async def get_items(
    limit: int = RECORDS_LIMIT,
    page: int = BASE_PAGE,
) -> Optional[List[Item]]:
    return [
        prepare_item_response(item_data)
        for item_data in bl_get_items.get_items(limit, page)
    ]


@json_router.post('/items/')
async def create_item(request: Request, item: CreateItem) -> Item:
    _item = bl_create_item.create_item(
        author_ip=request.client.host,
        name=item.name,
        description=item.description,
        count=item.items_count,
    )
    return prepare_item_response(_item)


@json_router.put('/items/{item_id}/')
async def update_item(item_id: int, item: UpdateItem) -> Item:
    _item = bl_update_item.update_item(
        item_id,
        name=item.name,
        description=item.description,
        count=item.items_count,
    )
    return prepare_item_response(_item)


@json_router.delete('/items/{item_id}/')
async def delete_item(item_id: int) -> Response:
    _is_deleted = bl_delete_item.delete_item(item_id)
    message = 'OK' if _is_deleted else 'Item: %s - Not found' % item_id
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={'message': message}
    )

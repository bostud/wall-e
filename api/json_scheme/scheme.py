import math
from typing import Optional

from pydantic import BaseModel, Field, validator, Extra


class CreateItem(BaseModel):
    class Config:
        extra = Extra.ignore

    name: str = Field(..., max_length=50)
    description: Optional[str] = Field(None, max_length=250)
    items_count: int = 0

    @validator('items_count')
    def validate_items_count(cls, v):
        max_value = math.pow(2, 31)

        if int(v) > max_value:
            raise ValueError('value must be lower that %s' % max_value)
        return v


class UpdateItem(CreateItem):
    item_id: int


class Item(UpdateItem):
    author_ip: str

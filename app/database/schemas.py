from typing import List, Optional

from pydantic import BaseModel, Json


# search products
class SearchTextBase(BaseModel):
    text: str


class SearchTextCreate(SearchTextBase):
    pass


class ProductListBase(BaseModel):
    # product: Json
    pass


class ProductListCreate(ProductListBase):
    pass


class ProductList(ProductListBase):
    id: int
    information: dict
    search_text_id: int

    class Config:
        orm_mode = True


# details

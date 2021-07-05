from typing import List, Optional

from pydantic import BaseModel


# search products
class ProductList(BaseModel):
    id: int
    information: dict
    search_text_id: int

    class Config:
        orm_mode = True


# details

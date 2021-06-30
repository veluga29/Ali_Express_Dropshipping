from typing import List, Optional

from pydantic import BaseModel, Json


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


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
    search_text_id: int
    
    class Config:
        orm_mode = True


# details



# security
class UserInDB(User):
    hashed_password: str
    


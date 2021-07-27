from typing import List, Optional

from pydantic import BaseModel, EmailStr


class SearchText(BaseModel):
    text: str


class SearchTextInput(SearchText):
    id: int
    page: int

    class Config:
        orm_mode = True


class SearchTextOutput(SearchText):
    class Config:
        orm_mode = True


# search products
class ProductList(BaseModel):
    id: int
    information: dict
    search_text_id: int

    class Config:
        orm_mode = True


# product details
class ProductDetail(BaseModel):
    id: int
    productUrl: str
    productId: str
    statusId: str
    status: str
    currency: str
    locale: str
    shipTo: str
    title: str
    totalStock: int
    totalOrders: int
    wishlistCount: int
    unitName: str
    unitNamePlural: str
    unitsPerProduct: int
    hasPurchaseLimit: bool
    maxPurchaseLimit: Optional[int]
    processingTimeInDays: int
    productImages: List[str]
    productCategory: dict
    seller: dict
    sellerDetails: dict
    hasSinglePrice: bool
    priceSummary: Optional[dict]  # optional하게 둬도 될지
    price: Optional[dict]
    hasAttributes: bool
    attributes: List[dict]
    hasReviewsRatings: bool
    reviewsRatings: dict
    hasProperties: bool
    properties: List[dict]
    hasVariations: bool
    variations: List[dict]
    shipping: dict
    htmlDescription: str

    class Config:
        orm_mode = True


# authentication
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: EmailStr


# accounts
class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

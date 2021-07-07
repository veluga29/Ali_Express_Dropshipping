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
    maxPurchaseLimit: int
    processingTimeInDays: int
    productImages: List[str]
    productCategory: dict
    seller: dict
    sellerDetails: dict
    hasSinglePrice: bool
    priceSummary: dict
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

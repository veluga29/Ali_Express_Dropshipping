from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


# HW
class SearchText(Base):
    __tablename__ = "search_texts"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    page = Column(Integer, default=1)
    
    product_list = relationship("ProductList", backref="search_text")


class ProductList(Base):
    __tablename__ = "product_lists"
    
    id = Column(Integer, primary_key=True, index=True)
    # 제품에 대한 정보들이 계층적으로 구성되어 있어, JSON으로 저장하는게 어떨까 생각했습니다.
    product = Column(JSON, index=True)
    search_text_id = Column(Integer, ForeignKey('search_texts.id'))
    
    
class ProductDetail(Base):
    __tablename__ = "product_details"
    
    id = Column(Integer, primary_key=True, index=True)
    productUrl = Column(String, index=True)
    productId = Column(String, index=True)
    statusId = Column(String, index=True)
    status = Column(String, index=True)
    currency = Column(String, index=True)
    locale = Column(String, index=True)
    shipTo = Column(String, index=True)
    title = Column(String, index=True)
    totalStock = Column(Integer, index=True)
    totalOrders = Column(Integer, index=True)
    wishlistCount = Column(Integer, index=True)
    unitName = Column(String, index=True)
    unitNamePlural = Column(String, index=True)
    unitsPerProduct = Column(Integer, index=True)
    hasPurchaseLimit = Column(Boolean, index=True)
    maxPurchaseLimit = Column(Integer, index=True)
    processingTimeInDays = Column(Integer, index=True)
    productImages = Column(String, index=True)  # list
    productCategory = Column(String, index=True)  # dict
    seller = Column(String, index=True)  # dict
    sellerDetails = Column(String, index=True)  # dict
    hasSinglePrice = Column(Boolean, index=True)
    price = Column(String, index=True)  # dict
    hasAttributes = Column(Boolean, index=True)
    attributes = Column(String, index=True)  # list
    hasReviewsRatings = Column(Boolean, index=True)
    reviewsRatings = Column(String, index=True)  # dict
    hasProperties = Column(Boolean, index=True)
    properties = Column(String, index=True)  # list
    hasVariations = Column(Boolean, index=True)
    variations = Column(String, index=True)  # list
    shipping = Column(String, index=True)  # dict
    htmlDescription = Column(String, index=True)
    priceSummary = Column(Integer, index=True)

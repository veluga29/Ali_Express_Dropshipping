import sqlalchemy as sa
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON, ARRAY
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from .database import Base


class AbstractBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    create_dt = Column(postgresql.TIMESTAMP(timezone=True), server_default=sa.func.now())
    update_dt = Column(postgresql.TIMESTAMP(timezone=True), onupdate=sa.func.now())


# HW
class SearchText(AbstractBase):
    __tablename__ = "search_texts"

    text = Column(String, index=True)
    page = Column(Integer, default=1)

    product_list = relationship("ProductList", back_populates="search_text")


class ProductList(AbstractBase):
    __tablename__ = "product_lists"

    # 제품에 대한 정보들이 계층적으로 구성되어 있어, JSON으로 저장하는게 어떨까 생각했습니다.
    information = Column(JSON, nullable=True)
    search_text_id = Column(Integer, ForeignKey("search_texts.id"))
    search_text = relationship("SearchText", back_populates="product_list")


class ProductDetail(AbstractBase):
    __tablename__ = "product_details"

    productUrl = Column(String, index=True)
    productId = Column(String, index=True)
    statusId = Column(String, index=True)
    status = Column(String, index=True)
    currency = Column(String, index=True)
    locale = Column(String, index=True)
    shipTo = Column(String, index=True)
    title = Column(String, index=True)
    totalStock = Column(Integer)
    totalOrders = Column(Integer)
    wishlistCount = Column(Integer)
    unitName = Column(String)
    unitNamePlural = Column(String)
    unitsPerProduct = Column(Integer)
    hasPurchaseLimit = Column(Boolean)
    maxPurchaseLimit = Column(Integer)
    processingTimeInDays = Column(Integer)
    productImages = Column(ARRAY(String), index=True)  # list
    productCategory = Column(JSON, index=True)  # dict
    seller = Column(JSON, index=True)  # dict
    sellerDetails = Column(JSON, index=True)  # dict
    hasSinglePrice = Column(Boolean, index=True)
    priceSummary = Column(JSON, index=True)  # dict, docs와 변수명이 다름
    hasAttributes = Column(Boolean, index=True)
    attributes = Column(ARRAY(JSON), index=True)  # list
    hasReviewsRatings = Column(Boolean, index=True)
    reviewsRatings = Column(JSON, index=True)  # dict
    hasProperties = Column(Boolean)
    properties = Column(ARRAY(JSON))  # list
    hasVariations = Column(Boolean)
    variations = Column(ARRAY(JSON))  # list
    shipping = Column(JSON)  # dict
    htmlDescription = Column(String)

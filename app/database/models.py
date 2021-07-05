import sqlalchemy as sa
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
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

import sqlalchemy as sa
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON, ARRAY
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

# from sqlalchemy_utils import EmailType

from .database import Base


class AbstractBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    create_dt = Column(postgresql.TIMESTAMP(timezone=True), server_default=sa.func.now())
    update_dt = Column(
        postgresql.TIMESTAMP(timezone=True), default=sa.func.now(), onupdate=sa.func.now()
    )


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

    productUrl = Column("product_url", String)
    productId = Column("product_id", String, index=True)
    statusId = Column("status_id", String)
    status = Column(String)
    currency = Column(String, index=True)
    locale = Column(String)
    shipTo = Column("ship_to", String, index=True)
    title = Column(String)
    totalStock = Column("total_stock", Integer)
    totalOrders = Column("total_orders", Integer)
    wishlistCount = Column("wishlist_count", Integer)
    unitName = Column("unit_name", String)
    unitNamePlural = Column("unit_name_plural", String)
    unitsPerProduct = Column("units_per_product", Integer)
    hasPurchaseLimit = Column("has_purchase_limit", Boolean, default=False)
    maxPurchaseLimit = Column("max_purchase_limit", Integer)
    processingTimeInDays = Column("processing_time_in_days", Integer)
    productImages = Column("product_images", JSON)  # list
    productCategory = Column("product_category", JSON)  # dict
    seller = Column(JSON)  # dict
    sellerDetails = Column("seller_details", JSON)  # dict
    hasSinglePrice = Column("has_single_price", Boolean)
    price = Column(JSON)
    priceSummary = Column("price_summary", JSON)  # dict, docs와 변수명이 다름
    hasAttributes = Column("has_attributes", Boolean)
    attributes = Column(JSON)  # list
    hasReviewsRatings = Column("has_reviews_ratings", Boolean)
    reviewsRatings = Column("reviews_ratings", JSON)  # dict
    hasProperties = Column("has_properties", Boolean)
    properties = Column(JSON)  # list
    hasVariations = Column("has_variations", Boolean)
    variations = Column(JSON)  # list
    shipping = Column(JSON)  # dict
    htmlDescription = Column("html_description", String)


class User(AbstractBase):
    __tablename__ = "users"

    user_id = Column(String(100), index=True, unique=True)
    # email = Column(EmailType, unique=True)
    hashed_password = Column(String(200))
    first_name = Column(String(30))
    last_name = Column(String(30))

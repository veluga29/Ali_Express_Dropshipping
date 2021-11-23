from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship

from app.models.base import AbstractBase


class SearchText(AbstractBase):
    __tablename__ = "search_texts"

    text = Column(String, index=True)
    page = Column(Integer, default=1)

    product_list = relationship("ProductList", back_populates="search_text")


class ProductList(AbstractBase):
    __tablename__ = "product_lists"

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
    productImages = Column("product_images", JSON)
    productCategory = Column("product_category", JSON)
    seller = Column(JSON)
    sellerDetails = Column("seller_details", JSON)
    hasSinglePrice = Column("has_single_price", Boolean)
    price = Column(JSON)
    priceSummary = Column("price_summary", JSON)
    hasAttributes = Column("has_attributes", Boolean)
    attributes = Column(JSON)
    hasReviewsRatings = Column("has_reviews_ratings", Boolean)
    reviewsRatings = Column("reviews_ratings", JSON)
    hasProperties = Column("has_properties", Boolean)
    properties = Column(JSON)
    hasVariations = Column("has_variations", Boolean)
    variations = Column(JSON)
    shipping = Column(JSON)
    htmlDescription = Column("html_description", String)

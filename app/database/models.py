from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
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
    __tablename__ = "search_text"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    
    product_lists = relationship("ProductLists", back_populates="search_text")

class ProductLists(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    # 제품에 대한 정보들이 계층적으로 구성되어 있어, JSON으로 저장하는게 합리적이라고 판단했습니다.
    product = Column(JSONB, index=True)  # JSON과 JSONB에 대하여 조사할 것
    search_text_id = Column(Integer, ForeignKey("search_text.id"))
    
    search_text = relationship("SearchText", back_populates="product_lists")
    
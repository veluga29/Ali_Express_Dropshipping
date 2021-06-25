from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
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
    __tablename__ = "Search_texts"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)

class ProductLists(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    #....
    
    search_text_id = Column(Integer, ForeignKey("search_texts.id"))
    
    search_text = relationship("SearchText", back_populates="product_lists")
    
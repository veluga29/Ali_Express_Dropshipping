from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas


# search functions
def create_search_text(db: Session, text: str, page: int):
    search_text = models.SearchText(text=text, page=page)
    db.add(search_text)
    db.commit()
    db.refresh(search_text)
    return search_text


def get_search_text_and_page(db: Session, text: str, page: int):
    return (
        db.query(models.SearchText)
        .filter(models.SearchText.text == text, models.SearchText.page == page)
        .first()
    )


def create_searched_products(db: Session, information: dict, search_text_id: int):  # schema 적용 필요
    db_item = models.ProductList(information=information, search_text_id=search_text_id)
    # print(db_item.information)
    # print(db_item.search_text_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_searched_products(db: Session, db_text_id):
    return (
        db.query(models.ProductList).filter(models.ProductList.search_text_id == db_text_id).all()
    )


# product details
def create_product_details(db: Session, db_item):  # schema 적용 필요
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas


# search functions
def create_search_text_with_product_list(db: Session, text: str, page: int, information: dict):
    db_text = models.SearchText(text=text, page=page)
    db.add(db_text)
    db.flush()
    db_product = models.ProductList(information=information, search_text_id=db_text.id)
    db.add(db_product)
    db.commit()
    return db_product


def get_search_text_and_page(db: Session, text: str, page: int):
    return (
        db.query(models.SearchText)
        .filter(models.SearchText.text == text, models.SearchText.page == page)
        .first()
    )


# def create_search_text(db: Session, text: str, page: int):
#     search_text = models.SearchText(text=text, page=page)
#     db.add(search_text)
#     db.commit()
#     return search_text


# def create_searched_products(db: Session, information: dict, search_text_id: int):
#     db_product = models.ProductList(information=information, search_text_id=search_text_id)
#     db.add(db_product)
#     db.commit()
#     return db_product


# def get_searched_products(db: Session, db_text_id):
#     return (
#         db.query(models.ProductList).filter(models.ProductList.search_text_id == db_text_id).all()
#     )


# product details
def create_product_details(db: Session, information: dict):
    db_item = models.ProductDetail(**information)
    db.add(db_item)
    db.commit()
    return db_item


def get_product_detail(db: Session, product_id: str):
    return (
        db.query(models.ProductDetail).filter(models.ProductDetail.productId == product_id).first()
    )

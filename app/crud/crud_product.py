from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate

from app.models import model_product


# search functions
def create_search_text_with_product_list(db: Session, text: str, page: int, information: dict):
    db_text = model_product.SearchText(text=text, page=page)
    db.add(db_text)
    db.flush()
    db_product = model_product.ProductList(information=information, search_text_id=db_text.id)
    db.add(db_product)
    db.commit()
    return db_product


def update_product_list(db: Session, search_text_id: int, information: dict):
    db_product_list = (
        db.query(model_product.ProductList).filter_by(search_text_id=search_text_id).first()
    )
    db_product_list.information = information
    db.commit()
    db.refresh(db_product_list)
    return db_product_list


def get_search_text_and_page(db: Session, text: str, page: int):
    return (
        db.query(model_product.SearchText)
        .filter(model_product.SearchText.text == text, model_product.SearchText.page == page)
        .first()
    )


# autocomplete search text
def get_search_text_like(db: Session, text: str):
    return paginate(
        db.query(model_product.SearchText)
        .filter(model_product.SearchText.text.like(f"%{text}%"))
        .distinct(model_product.SearchText.text)
    )


# product details
def create_product_details(db: Session, information: dict):
    db_item = model_product.ProductDetail(**information)
    db.add(db_item)
    db.commit()
    return db_item


def update_product_details(db: Session, product_id: str, information: dict):
    db_item = db.query(model_product.ProductDetail).filter_by(productId=product_id).first()
    for key, value in information.items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_product_detail(db: Session, product_id: str):
    return (
        db.query(model_product.ProductDetail)
        .filter(model_product.ProductDetail.productId == product_id)
        .first()
    )

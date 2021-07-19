from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import distinct
from sqlalchemy.orm import Session
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional

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


def update_product_list(db: Session, search_text_id: int, information: dict):
    db_product_list = db.query(models.ProductList).filter_by(search_text_id=search_text_id).first()
    db_product_list.information = information
    db.commit()
    return db_product_list


def get_search_text_and_page(db: Session, text: str, page: int):
    return (
        db.query(models.SearchText)
        .filter(models.SearchText.text == text, models.SearchText.page == page)
        .first()
    )


# autocomplete search text
def get_search_text_like(db: Session, text: str, page: int, limit: int):
    return (
        db.query(models.SearchText)
        .filter(models.SearchText.text.like(f"%{text}%"))
        .distinct(models.SearchText.text)
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )


# product details
def create_product_details(db: Session, information: dict):
    db_item = models.ProductDetail(**information)
    db.add(db_item)
    db.commit()
    return db_item


def update_product_details(db: Session, product_id: str, information: dict):
    # First way
    # db_item = db.query(models.ProductDetail).filter_by(productId=product_id).update(information)
    # db.commit()

    # Second way
    db_item = db.query(models.ProductDetail).filter_by(productId=product_id).first()
    for key, value in information.items():
        setattr(db_item, key, value)
    db.commit()
    return db_item


def get_product_detail(db: Session, product_id: str):
    return (
        db.query(models.ProductDetail).filter(models.ProductDetail.productId == product_id).first()
    )


# login_for_access_token
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(db: Session, user_id: str, password: str):
    user = db.query(models.User).filter_by(user_id=user_id).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(
    data: dict,
    token_secret_key: str,
    token_algorithm: str,
    expires_delta: Optional[timedelta] = None,
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, token_secret_key, algorithm=token_algorithm)
    return encoded_jwt

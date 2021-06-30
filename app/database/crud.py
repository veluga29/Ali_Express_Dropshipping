from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas
from ..dependencies import oauth2_scheme


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = "fakehashed"+ user.password
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, db_item: schemas.ItemCreate):
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# search functions
def create_search_text(db: Session, db_item: schemas.SearchTextCreate):
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_search_text(db: Session, text: str):
    return db.query(models.SearchText).filter(models.SearchText.text == text).first()


def create_searched_products(db: Session, db_item):  # schema 적용 필요
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_searched_products(db: Session, db_text_id):
    return db.query(models.ProductLists).filter(models.ProductLists.search_text_id == db_text_id).all()


# product details
def create_product_details(db: Session, db_item):  # schema 적용 필요
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# security
def fake_hash_password(password: str):
    return "fakehashed" + password


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return schemas.UserInDB(**user_dict)


def fake_decode_token(token):
    get_user_by_email(db, form_data.username)
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: schemas.User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

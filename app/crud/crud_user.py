from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.models.user import User
from app.schemas import user


# accounts
def get_user_by_email(db: Session, email: user.EmailStr):
    return db.query(User).filter_by(email=email).first()


def create_user(db: Session, user: user.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        password=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
    )
    db.add(db_user)
    db.commit()
    return db_user


def update_user(db: Session, db_user: User, update_data: user.UserUpdate):
    if update_data.password is not None:
        update_data.password = get_password_hash(update_data.password)
    update_data_dict = update_data.dict(exclude_unset=True)
    for key, value in update_data_dict.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, db_user: User):
    db.delete(db_user)
    db.commit()
    return db_user


# for super user
# def get_users(db: Session, skip: int, limit: int):
#     return db.query(User).offset(skip).limit(limit).all()

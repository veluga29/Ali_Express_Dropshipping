from sqlalchemy import Column, String
from sqlalchemy_utils import EmailType

from app.models.model import AbstractBase


class User(AbstractBase):
    __tablename__ = "users"

    email = Column(EmailType, index=True, unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    first_name = Column(String(30))
    last_name = Column(String(30))

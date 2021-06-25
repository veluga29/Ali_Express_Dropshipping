from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..settting import DB_HOST, DB_PORT, DB_USER_NAME, DB_USER_PASSWORD, DB_NAME


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER_NAME, DB_USER_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

import sqlalchemy as sa
from sqlalchemy import Column, Integer
from sqlalchemy.dialects import postgresql

from app.database import Base


class AbstractBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    create_dt = Column(postgresql.TIMESTAMP(timezone=True), server_default=sa.func.now())
    update_dt = Column(
        postgresql.TIMESTAMP(timezone=True), default=sa.func.now(), onupdate=sa.func.now()
    )

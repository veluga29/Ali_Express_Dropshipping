from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import json

from ..database import crud, schemas, models
from ..dependencies import get_db
from ..zapiex.zapiex import zapiex_apis

router = APIRouter(
    prefix="/details"
)


# model과 관련하여 수정할 부분이 많이 존재
@router.post("/")
def create_details(product_id: str, db: Session = Depends(get_db)):
    product_info = zapiex_apis.get_product(product_id)
    product_details = models.ProductDetails(**product_info['data'])
    return crud.create_product_details(db=db, db_item=product_details)
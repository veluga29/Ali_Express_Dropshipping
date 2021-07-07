from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from ..database import crud, schemas
from ..dependencies import get_db
from ..zapiex.zapiex import zapiex_apis

router = APIRouter(prefix="/details")


# @router.post("/", response_model=schemas.ProductDetail)
@router.post("/")
def create_details(product_id: str, db: Session = Depends(get_db)):
    try:
        db_detail = crud.get_product_detail(db, product_id=product_id)
        if db_detail:
            return db_detail
        product_info = zapiex_apis.get_product(product_id)
        if product_info["statusCode"] == 200:
            information = product_info["data"]
            return crud.create_product_details(db=db, information=information)
        else:
            raise HTTPException(
                status_code=product_info["statusCode"], detail=product_info["errorMessage"]
            )
    except Exception:
        raise

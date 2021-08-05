from fastapi import APIRouter, Depends, Query
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi_pagination import Page

from app.crud import crud_product
from app.schemas import pyd_product
from app.dependencies import get_current_user, get_db
from app.utils.zapiex import zapiex_apis


router = APIRouter(prefix="/products", tags=["products"])


"""
{
    cur: "http://localhost:8000/products?text=cat&pg=1&count=20"
    next: "http://localhost:8000/products?text=cat&pg=2&count=15"
    data: [{
        
    }]
}
"""


@router.get("/", dependencies=[Depends(get_current_user)], response_model=pyd_product.ProductList)
async def search_items_by_text(text: str, page: int, db: Session = Depends(get_db)):
    try:
        search_text = crud_product.get_search_text_and_page(db, text=text, page=page)
        if search_text:
            product_list = search_text.product_list[0]
            if product_list.update_dt >= datetime.utcnow() - timedelta(days=1):
                return search_text.product_list[0]
            search_info = zapiex_apis.search_products(text, page)
            status_code = search_info["statusCode"]
            information = search_info["data"]
            if status_code == 200:
                return crud_product.update_product_list(
                    db, search_text_id=search_text.id, information=information
                )
        search_info = zapiex_apis.search_products(text, page)
        status_code = search_info["statusCode"]
        information = search_info["data"]
        if status_code == 200:
            return crud_product.create_search_text_with_product_list(
                db=db, text=text, page=page, information=information
            )
        else:
            raise HTTPException(status_code=status_code, detail=search_info["errorMessage"])
    except Exception:
        raise


@router.get(
    "/search",
    dependencies=[Depends(get_current_user)],
    response_model=Page[pyd_product.SearchTextOutput],
)
def autocomplete_search_text(
    search: str = Query(..., max_length=50, regex="[A-Za-z0-9]"), db: Session = Depends(get_db)
):
    try:
        return crud_product.get_search_text_like(db, text=search)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)


@router.get(
    "/{product_id}",
    dependencies=[Depends(get_current_user)],
    response_model=pyd_product.ProductDetail,
)
def create_details(product_id: str, db: Session = Depends(get_db)):
    try:
        db_detail = crud_product.get_product_detail(db, product_id=product_id)
        if db_detail:
            if db_detail.update_dt >= datetime.utcnow() - timedelta(days=1):
                return db_detail
            product_info = zapiex_apis.get_product(product_id)
            status_code = product_info["statusCode"]
            information = product_info["data"]
            # active 이외의 status에 대해 return 하지 않아도 될까요?
            if status_code == 200 and information["status"] != "active":
                return
            if status_code == 200:
                return crud_product.update_product_details(
                    db=db, product_id=product_id, information=information
                )
            elif status_code == 201:
                raise HTTPException(status_code=status_code)
            else:
                raise HTTPException(status_code=status_code, detail=product_info["errorMessage"])
        product_info = zapiex_apis.get_product(product_id)
        status_code = product_info["statusCode"]
        information = product_info["data"]
        # active 이외의 status에 대해 else로 return 하지 않아도 될까요?
        if status_code == 200 and information["status"] != "active":
            return
        if status_code == 200:
            return crud_product.create_product_details(db=db, information=information)
        elif status_code == 201:
            # ex) '1230192314802471024333333333332433256164', 'asdf5625435', ';;;;'
            return  # 이렇게 케이스를 나눈 상황에서 null 값 리턴해도 상관없을지 고민됩니다. (schema로 인해 리턴값이 제한됨)
        else:
            # ex) '강아지'
            raise HTTPException(status_code=status_code, detail=product_info["errorMessage"])
    except Exception:
        raise

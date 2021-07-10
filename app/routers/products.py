from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from ..database import crud, schemas, models
from ..dependencies import get_db
from ..zapiex.zapiex import zapiex_apis

router = APIRouter(prefix="/products", tags=["products"])

""" HW July 3rd
1. When SearchText is stored but ProductList isn't, return [] -> Please making sure both SearchText and ProductList are stored 
2. Search API analysis
3. crud, model, router setting for ProductDetail API
4. Schemas setting for search, ProductDetail, SearchText
"""


@router.post("/", response_model=schemas.ProductList)
async def search_items_by_text(text: str, page: int, db: Session = Depends(get_db)):
    try:
        search_text = crud.get_search_text_and_page(db, text=text, page=page)
        # 이미 검색한 기록이 있으면 db에서 꺼내 보여줌
        if search_text:
            return search_text.product_list[0]
        search_info = zapiex_apis.search_products(text, page)  # Zapiex API 호출
        if search_info["statusCode"] == 200:
            information = search_info["data"]
            return crud.create_search_text_with_product_list(
                db=db, text=text, page=page, information=information
            )
            # code before
            # search_text = crud.create_search_text(
            #     db=db, text=text, page=page
            # )
            # information = search_info["data"]
            # return crud.create_searched_products(
            #     db=db, information=information, search_text_id=search_text.id
            # )
        else:
            raise HTTPException(
                status_code=search_info["statusCode"], detail=search_info["errorMessage"]
            )
    except Exception:
        raise


@router.post("/{product_id}", response_model=schemas.ProductDetail)
def create_details(product_id: str, db: Session = Depends(get_db)):
    try:
        db_detail = crud.get_product_detail(db, product_id=product_id)
        if db_detail:
            return db_detail
        product_info = zapiex_apis.get_product(product_id)
        if product_info["statusCode"] == 200:
            information = product_info["data"]
            if information["status"] == "active":  # active 이외의 status에 대해 else로 return 하지 않아도 될까요?
                return crud.create_product_details(db=db, information=information)
        elif product_info["statusCode"] == 201:
            # ex) '1230192314802471024333333333332433256164', 'asdf5625435', ';;;;'
            return  # 이렇게 케이스를 나눈 상황에서 null 값 리턴해도 상관없을지 고민됩니다. (schema로 인해 리턴값이 제한됨)
        else:
            # ex) '강아지'
            raise HTTPException(
                status_code=product_info["statusCode"], detail=product_info["errorMessage"]
            )
    except Exception:
        raise

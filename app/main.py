from fastapi import FastAPI

from .database import models
from .database.database import engine
from .routers import items, users, search, security


def create_app():
    app = FastAPI()

    # 데이터 베이스 이니셜라이즈
    models.Base.metadata.create_all(bind=engine)
    
    # 라우터 정의
    app.include_router(items.router)
    app.include_router(users.router)
    app.include_router(search.router)
    app.include_router(security.router)

    return app

app = create_app()


@app.get("/")
async def root():
    return {"message": "Ali express dropshipping"}

import uvicorn
from fastapi import FastAPI

from app.database import models
from app.database.database import engine
from app.routers import authentication, products


def create_app():
    app = FastAPI()

    # 데이터 베이스 이니셜라이즈
    models.Base.metadata.create_all(bind=engine)

    # 라우터 정의
    app.include_router(products.router)
    app.include_router(authentication.router)

    return app


app = create_app()


@app.get("/")
async def root():
    return {"message": "Ali express dropshipping"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

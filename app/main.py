from fastapi import FastAPI

from app.api.routers.router import router
from app.config.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

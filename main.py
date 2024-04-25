from fastapi import FastAPI
from config.database import Base, engine
from databases import Database
from config.router import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

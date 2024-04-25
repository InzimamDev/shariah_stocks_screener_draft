import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for your models
Base = declarative_base()

def create_db_engine():
  print("asass")
  is_prod = os.environ.get("IS_PROD", False)
  if not is_prod:
      # Use .env file with load_dotenv for development
      from dotenv import load_dotenv

      load_dotenv()  # Load environment variables from .env file (development only)

  # Use environment variables directly for production
  db_username = os.environ.get("DB_USERNAME")
  db_password = os.environ.get("DB_PASSWORD")
  db_host = os.environ.get("DB_HOST")
  db_port = os.environ.get("DB_PORT", 5432)  # Default to 5432 for PostgreSQL
  db_name = os.environ.get("DB_NAME")

  DATABASE_URL = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

  engine = create_engine(DATABASE_URL)

  return engine
engine = create_db_engine()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

db_dependency = Annotated[Session, Depends(get_db)]

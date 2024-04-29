# Sharia stock screener

## Prerequisites

- Python 3.11
- PostgresSQL 15

## Get started

- Create a python virtual environment
- Activate environment
- Add a .env file with the following variables

```
  DB_USERNAME
  DB_PASSWORD
  DB_HOST
  DB_PORT
  DB_NAME
  IS_PROD
  DATABASE_URL
  DEBUG
```

- `pip3 install -r requirements.txt`
- `alembic upgrade head`
- `uvicorn app.main:app --reload`

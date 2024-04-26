from pydantic import BaseModel


class CompanyPost(BaseModel):
    cik: int
    ticker: str
    name: str
    website: str
    test_col: str
    test_new_col: str

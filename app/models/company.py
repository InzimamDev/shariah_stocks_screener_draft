from sqlalchemy import Column, Integer, String, UniqueConstraint
from app.config.database import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    cik = Column(Integer, unique=True)
    ticker = Column(String, unique=True)
    name = Column(String)
    website = Column(String, nullable=True)
    test_col = Column(String, nullable=True)
    test_new_col = Column(String, nullable=True)

    __table_args__ = (UniqueConstraint(
        'ticker', name='company_ticker_unique'),)

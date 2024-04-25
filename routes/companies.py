
from fastapi import APIRouter
from config.database import db_dependency
from models.company import Company
from schemas.company import CompanyPost

companies_router = APIRouter()

# Route to create a new company (POST /companies)
@companies_router.post("/companies")
async def create_company(company_data: CompanyPost, db: db_dependency):
    # Add company to database
    db_company = Company(**company_data.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)  # Refresh object to get generated ID
    return db_company


# Route to get a company by ID (GET /companies/{company_id})
@companies_router.get("/companies/{company_id}")
async def get_company(company_id: int, db: db_dependency):
    # Get the company from the database
    company = db.query(Company).filter(Company.id == company_id).first()

    # Check if company exists
    if company is None:
        return {"detail": f"Company with id {company_id} not found"}

    return company

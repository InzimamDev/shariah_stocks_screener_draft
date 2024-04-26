"""Companies file"""
from fastapi import APIRouter
from app.config.database import DatabaseDependency
from app.models.company import Company
from app.schemas.company import CompanyPost

company_module = APIRouter()

# Route to create a new company (POST /companies)


@company_module.post("/")
async def create_company(company_data: CompanyPost, db: DatabaseDependency):
    # Add company to database
    db_company = Company(**company_data.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)  # Refresh object to get generated ID
    return db_company


# Route to get a company by ID (GET /companies/{company_id})
@company_module.get("/{company_id}")
async def get_company(company_id: int, db: DatabaseDependency):
    # Get the company from the database
    company = db.query(Company).filter(Company.id == company_id).first()

    # Check if company exists
    if company is None:
        return {"detail": f"Company with id {company_id} not found"}

    return company

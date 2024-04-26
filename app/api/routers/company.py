from fastapi import APIRouter
from app.api.endpoints.company.company import company_module

company_router = APIRouter()

company_router.include_router(
    company_module,
    prefix="/companies",
    tags=["companies"],
    responses={404: {"description": "Not found"}},
)

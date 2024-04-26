from fastapi import APIRouter
from .company import company_router

router = APIRouter()

# Include all routers
router.include_router(company_router)
# ... include other routers

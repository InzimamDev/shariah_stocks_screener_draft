from fastapi import APIRouter
from routes.companies import companies_router

router = APIRouter()

# Include all routers
router.include_router(companies_router)
# ... include other routers

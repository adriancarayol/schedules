from fastapi import APIRouter

from api.routes import healthcheck

router = APIRouter()
router.include_router(healthcheck.router, tags=["healthcheck"], prefix="/healthcheck")

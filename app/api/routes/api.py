from fastapi import APIRouter

from api.routes import healthcheck, schedules

router = APIRouter()
router.include_router(healthcheck.router, tags=["healthcheck"], prefix="/healthcheck")
router.include_router(schedules.router, tags=["schedules"], prefix="/schedules")

from fastapi import APIRouter

from models.schemas.healthcheck import HealthCheck

router = APIRouter()


@router.get("", response_model=HealthCheck, name="healthcheck:health-check")
async def healthcheck() -> HealthCheck:
    return HealthCheck(message="Healthy")

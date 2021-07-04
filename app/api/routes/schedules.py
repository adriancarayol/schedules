from fastapi import APIRouter, HTTPException
from loguru import logger
from starlette import status

from models.domain.exceptions import InvalidOpeningHoursException
from models.schemas.schedules import OpeningHoursIn, OpeningHoursOut
from services.schedules import format_opening_hours, humanize_opening_hours

router = APIRouter()


@router.post("", response_model=OpeningHoursOut, name="schedules:opening-hours")
async def parse_opening_hours(opening_hours: OpeningHoursIn) -> OpeningHoursOut:
    logger.info(f"Attempt to parse opening hours: {opening_hours}")

    try:
        humanized_opening_hours = humanize_opening_hours(opening_hours)
        return format_opening_hours(humanized_opening_hours)
    except InvalidOpeningHoursException as e:
        logger.info(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

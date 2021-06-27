from fastapi import APIRouter

from models.schemas.schedules import OpeningHoursIn, OpeningHoursOut

router = APIRouter()


@router.post("", response_model=OpeningHoursOut, name="schedules:opening-hours")
async def parse_opening_hours(opening_hours: OpeningHoursIn) -> OpeningHoursOut:
    return OpeningHoursOut(day="Monday")

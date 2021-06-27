from typing import Dict, List

from pydantic import BaseModel, validator

from models.domain.schedules import (
    MAX_SECONDS_VALUE,
    MIN_SECONDS_VALUE,
    SCHEDULE_TYPES,
    WEEK_DAYS,
)


class OpeningHourIn(BaseModel):
    type: str
    value: int

    @validator("type")
    def validate_type(cls, v: str) -> str:
        if v not in SCHEDULE_TYPES:
            allowed_types = ", ".join(SCHEDULE_TYPES)
            raise ValueError(f"{v} is not in {allowed_types}")

        return v

    @validator("value")
    def validate_value(cls, v: int) -> int:
        if not MIN_SECONDS_VALUE <= v <= MAX_SECONDS_VALUE:
            raise ValueError(
                f"{v} is not between {MIN_SECONDS_VALUE} and {MAX_SECONDS_VALUE}"
            )
        return v


class OpeningHoursIn(BaseModel):
    opening_hours: Dict[str, List[OpeningHourIn]]

    @validator("opening_hours")
    def validate_week_names(
        cls, v: Dict[str, List[OpeningHourIn]]
    ) -> Dict[str, List[OpeningHourIn]]:
        for week_name, _ in v.items():
            if not week_name:
                raise ValueError("Week name cannot be empty.")
            if week_name not in WEEK_DAYS:
                allowed_week_days = ", ".join(WEEK_DAYS)
                raise ValueError(f"{v} is not in {allowed_week_days}.")

        return v


class OpeningHoursOut(BaseModel):
    day: str

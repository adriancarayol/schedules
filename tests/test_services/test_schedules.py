import pytest

from models.domain.exceptions import InvalidOpeningHoursException
from models.domain.schedules import OpeningHour
from models.schemas.schedules import (
    OpeningHoursIn,
    OpeningHourIn,
    OpeningHoursOut,
)
from services.schedules import (
    humanize_opening_hours,
    format_opening_hours,
)


@pytest.mark.parametrize(
    "opening_hours",
    [
        None,
        OpeningHoursIn(opening_hours={}),
        OpeningHoursIn(
            opening_hours={
                "monday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "tuesday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "wednesday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "thursday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "friday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "saturday": [
                    OpeningHourIn(type="open", value=6000),
                ],
            }
        ),
        OpeningHoursIn(
            opening_hours={
                "monday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="open", value=6000),
                ],
                "tuesday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "wednesday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "thursday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "friday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "saturday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "sunday": [
                    OpeningHourIn(type="open", value=6000),
                ],
            }
        ),
        OpeningHoursIn(
            opening_hours={
                "monday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "tuesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "wednesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "thursday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "friday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "saturday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "sunday": [
                    OpeningHourIn(type="open", value=6000),
                ],
            }
        ),
        OpeningHoursIn(
            opening_hours={
                "monday": [
                    OpeningHourIn(type="close", value=6001),
                ],
                "tuesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "wednesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "thursday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "friday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "saturday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "sunday": [
                    OpeningHourIn(type="open", value=6000),
                ],
            }
        ),
        OpeningHoursIn(
            opening_hours={
                "monday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                    OpeningHourIn(type="close", value=6002),
                ],
                "tuesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "wednesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "thursday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "friday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "saturday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "sunday": [
                    OpeningHourIn(type="open", value=6000),
                ],
            }
        ),
        OpeningHoursIn(
            opening_hours={
                "monday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "tuesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "wednesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "thursday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "friday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "saturday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "sunday": [
                    OpeningHourIn(type="open", value=6000),
                ],
            }
        ),
        OpeningHoursIn(
            opening_hours={
                "monday": [
                    OpeningHourIn(type="close", value=6000),
                ],
                "tuesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "wednesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "thursday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "friday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "saturday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "sunday": [],
            }
        ),
        OpeningHoursIn(
            opening_hours={
                "monday": [
                    OpeningHourIn(type="close", value=6000),
                ],
                "tuesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "wednesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "thursday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "friday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "saturday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "sunday": [
                    OpeningHourIn(type="close", value=6000),
                ],
            }
        ),
        OpeningHoursIn(
            opening_hours={
                "monday": [
                    OpeningHourIn(type="close", value=6000),
                ],
                "tuesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "wednesday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "thursday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "friday": [
                    OpeningHourIn(type="open", value=6000),
                    OpeningHourIn(type="close", value=6001),
                ],
                "saturday": [
                    OpeningHourIn(type="open", value=6000),
                ],
                "sunday": [
                    OpeningHourIn(type="close", value=6001),
                    OpeningHourIn(type="open", value=6002),
                    OpeningHourIn(type="close", value=6003),
                ],
            }
        ),
    ],
)
def test_humanize_opening_hours_days_invalid(opening_hours):
    with pytest.raises(InvalidOpeningHoursException):
        humanize_opening_hours(opening_hours)


@pytest.mark.parametrize(
    "opening_hours, expected",
    [
        (
            OpeningHoursIn(
                opening_hours={
                    "monday": [],
                    "tuesday": [],
                    "wednesday": [],
                    "thursday": [],
                    "friday": [],
                    "saturday": [],
                    "sunday": [],
                }
            ),
            OpeningHour(
                opening_hours={
                    "monday": [],
                    "tuesday": [],
                    "wednesday": [],
                    "thursday": [],
                    "friday": [],
                    "saturday": [],
                    "sunday": [],
                }
            ),
        ),
        (
            OpeningHoursIn(
                opening_hours={
                    "monday": [
                        OpeningHourIn(type="open", value=36000),
                        OpeningHourIn(type="close", value=64800),
                        OpeningHourIn(type="open", value=64801),
                        OpeningHourIn(type="close", value=68800),
                    ],
                    "tuesday": [],
                    "wednesday": [],
                    "thursday": [],
                    "friday": [],
                    "saturday": [],
                    "sunday": [],
                }
            ),
            OpeningHour(
                opening_hours={
                    "monday": [
                        ("10:00:00 AM", "06:00:00 PM"),
                        ("06:00:01 PM", "07:06:40 PM"),
                    ],
                    "tuesday": [],
                    "wednesday": [],
                    "thursday": [],
                    "friday": [],
                    "saturday": [],
                    "sunday": [],
                }
            ),
        ),
        (
            OpeningHoursIn(
                opening_hours={
                    "monday": [],
                    "tuesday": [
                        OpeningHourIn(type="open", value=36000),
                        OpeningHourIn(type="close", value=64800),
                    ],
                    "wednesday": [],
                    "thursday": [
                        OpeningHourIn(type="open", value=37800),
                        OpeningHourIn(type="close", value=64800),
                    ],
                    "friday": [
                        OpeningHourIn(type="open", value=36000),
                    ],
                    "saturday": [
                        OpeningHourIn(type="close", value=3600),
                        OpeningHourIn(type="open", value=36000),
                    ],
                    "sunday": [
                        OpeningHourIn(type="close", value=3600),
                        OpeningHourIn(type="open", value=43200),
                        OpeningHourIn(type="close", value=75600),
                    ],
                }
            ),
            OpeningHour(
                opening_hours={
                    "monday": [],
                    "tuesday": [["10:00:00 AM", "06:00:00 PM"]],
                    "wednesday": [],
                    "thursday": [["10:30:00 AM", "06:00:00 PM"]],
                    "friday": [["10:00:00 AM", "01:00:00 AM"]],
                    "saturday": [["10:00:00 AM", "01:00:00 AM"]],
                    "sunday": [["12:00:00 PM", "09:00:00 PM"]],
                }
            ),
        ),
        (
            OpeningHoursIn(
                opening_hours={
                    "monday": [
                        OpeningHourIn(type="close", value=3600),
                    ],
                    "tuesday": [
                        OpeningHourIn(type="open", value=36000),
                        OpeningHourIn(type="close", value=64800),
                    ],
                    "wednesday": [],
                    "thursday": [
                        OpeningHourIn(type="open", value=37800),
                        OpeningHourIn(type="close", value=64800),
                    ],
                    "friday": [
                        OpeningHourIn(type="open", value=36000),
                    ],
                    "saturday": [
                        OpeningHourIn(type="close", value=3600),
                        OpeningHourIn(type="open", value=36000),
                    ],
                    "sunday": [
                        OpeningHourIn(type="close", value=3600),
                        OpeningHourIn(type="open", value=43200),
                    ],
                }
            ),
            OpeningHour(
                opening_hours={
                    "monday": [],
                    "tuesday": [["10:00:00 AM", "06:00:00 PM"]],
                    "wednesday": [],
                    "thursday": [["10:30:00 AM", "06:00:00 PM"]],
                    "friday": [["10:00:00 AM", "01:00:00 AM"]],
                    "saturday": [["10:00:00 AM", "01:00:00 AM"]],
                    "sunday": [["12:00:00 PM", "01:00:00 AM"]],
                }
            ),
        ),
        (
            OpeningHoursIn(
                opening_hours={
                    "monday": [],
                    "tuesday": [],
                    "wednesday": [],
                    "thursday": [
                        OpeningHourIn(type="open", value=37800),
                        OpeningHourIn(type="close", value=64800),
                    ],
                    "friday": [
                        OpeningHourIn(type="open", value=36000),
                    ],
                    "saturday": [
                        OpeningHourIn(type="close", value=3600),
                        OpeningHourIn(type="open", value=36000),
                    ],
                    "sunday": [
                        OpeningHourIn(type="close", value=3600),
                    ],
                }
            ),
            OpeningHour(
                opening_hours={
                    "monday": [],
                    "tuesday": [],
                    "wednesday": [],
                    "thursday": [["10:30:00 AM", "06:00:00 PM"]],
                    "friday": [["10:00:00 AM", "01:00:00 AM"]],
                    "saturday": [["10:00:00 AM", "01:00:00 AM"]],
                    "sunday": [],
                }
            ),
        ),
    ],
)
def test_humanize_opening_hours_days(opening_hours, expected):
    result = humanize_opening_hours(opening_hours)
    assert result == expected


@pytest.mark.parametrize(
    "opening_hours, expected",
    [
        (
            OpeningHour(
                opening_hours={
                    "monday": [],
                    "tuesday": [],
                    "wednesday": [],
                    "thursday": [["10:30:00 AM", "06:00:00 PM"]],
                    "friday": [["10:00:00 AM", "01:00:00 AM"]],
                    "saturday": [["10:00:00 AM", "01:00:00 AM"]],
                    "sunday": [],
                }
            ),
            OpeningHoursOut(
                opening_hours={
                    "monday": "Closed",
                    "tuesday": "Closed",
                    "wednesday": "Closed",
                    "thursday": "10:30:00 AM - 06:00:00 PM",
                    "friday": "10:00:00 AM - 01:00:00 AM",
                    "saturday": "10:00:00 AM - 01:00:00 AM",
                    "sunday": "Closed",
                }
            ),
        ),
        (
            OpeningHour(
                opening_hours={
                    "tuesday": [],
                    "monday": [],
                    "wednesday": [],
                    "thursday": [
                        ["10:30:00 AM", "06:00:00 PM"],
                        ["06:05:00 PM", "09:00:00 PM"],
                    ],
                    "friday": [["10:00:00 AM", "01:00:00 AM"]],
                    "saturday": [["10:00:00 AM", "01:00:00 AM"]],
                    "sunday": [],
                }
            ),
            OpeningHoursOut(
                opening_hours={
                    "monday": "Closed",
                    "tuesday": "Closed",
                    "wednesday": "Closed",
                    "thursday": "10:30:00 AM - 06:00:00 PM, 06:05:00 PM - 09:00:00 PM",
                    "friday": "10:00:00 AM - 01:00:00 AM",
                    "saturday": "10:00:00 AM - 01:00:00 AM",
                    "sunday": "Closed",
                }
            ),
        ),
    ],
)
def test_format_opening_hours(opening_hours, expected):
    result = format_opening_hours(opening_hours)
    assert result == expected

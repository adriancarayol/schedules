import pytest

from pydantic import ValidationError


from models.schemas.schedules import (
    OpeningHoursIn,
    OpeningHourIn,
)


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            {
                "monday": [
                    {
                        "type": "open",
                        "value": 82000,
                    },
                ]
            },
            OpeningHoursIn(
                opening_hours={
                    "monday": [
                        OpeningHourIn(type="open", value="82000"),
                    ]
                }
            ),
        ),
        (
            {
                "monday": [
                    {
                        "type": "open",
                        "value": 82000,
                    },
                ],
                "tuesday": [
                    {
                        "type": "open",
                        "value": 82000,
                    },
                    {
                        "type": "close",
                        "value": 82001,
                    },
                ],
            },
            OpeningHoursIn(
                opening_hours={
                    "monday": [
                        OpeningHourIn(type="open", value="82000"),
                    ],
                    "tuesday": [
                        OpeningHourIn(type="open", value="82000"),
                        OpeningHourIn(type="close", value="82001"),
                    ],
                }
            ),
        ),
    ],
)
def test_opening_hours_in_model(input, expected):
    opening_hours = OpeningHoursIn(opening_hours=input)
    assert opening_hours == expected


@pytest.mark.parametrize(
    "input",
    [
        {
            "Monday": [
                {
                    "type": "open",
                    "value": 82000,
                },
            ]
        },
        {
            "Fake": [
                {
                    "type": "open",
                    "value": 82000,
                },
            ]
        },
        {
            "": [
                {
                    "type": "open",
                    "value": 82000,
                },
            ]
        },
    ],
)
def test_opening_hours_in_model_invalid_data(input):
    with pytest.raises(ValidationError):
        OpeningHoursIn(opening_hours=input)



@pytest.mark.parametrize("type_input, value_input", [
    ("open", -1),
    ("open", 900000),
    ("close", -1),
    ("close", 90000),
    ("xxx", -1),
    ("xxx", 1),
]
)
def test_opening_hour_in_model_invalid_data(type_input, value_input):
    with pytest.raises(ValidationError):
        OpeningHourIn(type=type_input, value=value_input)

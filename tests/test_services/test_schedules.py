import pytest

from services.schedules import humanize_opening_hours


@pytest.mark.parametrize(
    "opening_hours, expected",
    [
        ({}, {}),
    ],
)
def test_humanize_opening_hours(opening_hours, expected):
    result = humanize_opening_hours(opening_hours)

    assert result == expected

import pytest

from core.time import humanize_seconds


@pytest.mark.parametrize(
    "seconds, expected",
    [
        (32400, "09:00:00 AM"),
        (37800, "10:30:00 AM"),
        (86399, "11:59:59 PM"),
        (0, "12:00:00 AM"),
    ],
)
def test_humanize_seconds(seconds, expected):
    result = humanize_seconds(seconds)
    assert result == expected

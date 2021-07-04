from collections import OrderedDict
from typing import List, Tuple

from core.time import humanize_seconds
from models.domain.exceptions import InvalidOpeningHoursException
from models.domain.schedules import (
    CLOSE,
    OPEN,
    WEEK_DAYS,
    WEEK_DAYS_TRANSITIONS,
    OpeningHour,
)
from models.schemas.schedules import OpeningHourIn, OpeningHoursIn, OpeningHoursOut


def format_opening_hours(opening_hours: OpeningHour) -> OpeningHoursOut:
    """
    Format opening_hours humanized to string format.
    :params opening_hours: Opening hours humanized.
    :returns: Opening hours in string format.
    """

    opening_hours_formatted = OpeningHoursOut(opening_hours={})

    for week_day, schedules in opening_hours.opening_hours.items():
        if not schedules:
            opening_hours_formatted.opening_hours[week_day] = "Closed"
            continue

        str_schedules = []
        for schedule in schedules:
            str_schedules.append(" - ".join(schedule))

        opening_hours_formatted.opening_hours[week_day] = ", ".join(str_schedules)

    ordered_dict = OrderedDict(
        sorted(
            opening_hours_formatted.opening_hours.items(),
            key=lambda s: WEEK_DAYS.index(s[0]),
        )
    )

    return OpeningHoursOut(opening_hours=ordered_dict)


def humanize_opening_hours(opening_hours: OpeningHoursIn) -> OpeningHour:
    """
    Given a dictionary of opening hours,
    it returns a dictionary of opening hours humanized.
    Must be present every day of the week in the dictionary,
    in other case, an exception of type InvalidOpeningHoursException will be raised.

    For example:
    {
        "monday": [
            {
                "type": "open",
                "value": 36000,
            },
            {
                "type": "close",
                "value": 64800,
            },
        ],
        ...
    }
    will returns:
    "tuesday": [["10:00:00 AM", "06:00:00 PM"]],

    :params opening_hours:
    :returns: Opening hours humanized
    """

    if not opening_hours:
        raise InvalidOpeningHoursException("Provide a valid opening hours.")

    week_days = [week_day for week_day in opening_hours.opening_hours.keys()]

    if not _validate_opening_hours_for_all_days(week_days):
        raise InvalidOpeningHoursException("Please, provide opening hours for all days")

    humanized_scheduled = OpeningHour(opening_hours={k: [] for k in week_days})

    # Just sort the opening hours by value desc, so we can detect easily
    # the correct order of the schedules (open -> close -> open -> close, ...).
    _sort_opening_hours_by_value(opening_hours)

    for week_day, schedules in opening_hours.opening_hours.items():
        last_schedule_seen = None
        schedules_used_in_next_day = []

        if not schedules:
            continue

        while schedules:
            schedule = schedules.pop()
            last_schedule_type_seen = getattr(last_schedule_seen, "type", None)

            is_valid_opening_closing_time = True

            if not _validate_opening_and_closing_time(
                last_schedule_type_seen, schedule.type
            ):
                is_valid_opening_closing_time = False

            if not is_valid_opening_closing_time and _opening_time_from_prev_day(
                week_day, opening_hours
            ):
                schedules_used_in_next_day.append(schedule)
                continue

            if not is_valid_opening_closing_time:
                raise InvalidOpeningHoursException(
                    "Invalid opening hour detected: "
                    f"{last_schedule_type_seen} - {schedule.type}"
                )

            if last_schedule_seen and last_schedule_type_seen == OPEN:
                humanized_scheduled.opening_hours[week_day].append(
                    _humanized_opening_hours(last_schedule_seen.value, schedule.value)
                )

            last_schedule_seen = schedule

        if last_schedule_seen and last_schedule_seen.type == OPEN:
            opening_hour = _closing_time_from_next_day(week_day, opening_hours)

            humanized_scheduled.opening_hours[week_day].append(
                _humanized_opening_hours(last_schedule_seen.value, opening_hour.value)
            )

        schedules.extend(schedules_used_in_next_day)

    return humanized_scheduled


def _validate_opening_hours_for_all_days(week_days: List[str]) -> bool:
    """
    Validates that all the week days have opening hours.
    :params week_days: List of week days
    :returns: True if all the week days have opening hours, False in other case.
    """

    return all(day in week_days for day in WEEK_DAYS)


def _sort_opening_hours_by_value(
    opening_hours: OpeningHoursIn,
) -> None:
    """
    Sort the pening_hours input sorted by value desc.
    :params opening_hours: List of opening hours
    :returns: List of opening hours sorted by value.
    """
    for week_day, schedules in opening_hours.opening_hours.items():
        sorted_schedules = sorted(schedules, key=lambda s: s.value, reverse=True)
        opening_hours.opening_hours.update({week_day: sorted_schedules})


def _humanized_opening_hours(opening_hour: str, closing_time: str) -> Tuple[str, str]:
    """
    Returns a tuple of opening_hour, closing_time humanized.
    :params opening_hour: Opening hour in UNIX time.
    :params closing_time: Closing hour in UNIX time.
    :returns: Humanized tuple of opening_hour, closing time.
    """

    return (
        humanize_seconds(opening_hour),
        humanize_seconds(closing_time),
    )


def _closing_time_from_next_day(
    week_day: str, opening_hours: OpeningHoursIn
) -> OpeningHourIn:
    """
    Returns the closing time from the next day.
    It raises an exception if the next day does not have closing time for week_day.

    :params week_day: Week day from which want to retrieve the closing time.
    :params opening_hours: Opening hours of all the days.
    :returns: If the next day have close time, returns the closing time.
    """

    next_day = WEEK_DAYS_TRANSITIONS.get(week_day)
    next_day_opening_hour = opening_hours.opening_hours.get(next_day)

    if not next_day_opening_hour:
        raise InvalidOpeningHoursException(f"No closing time for day: {week_day}")

    opening_hour = next_day_opening_hour.pop()

    if opening_hour.type != CLOSE:
        raise InvalidOpeningHoursException(f"No closing time for day: {week_day}")

    return opening_hour


def _opening_time_from_prev_day(
    week_day: str, opening_hours: OpeningHoursIn
) -> OpeningHourIn:
    """
    Returns the opening time from the previous day.
    It raises an exception if the previous day does not have opening time for week_day.

    :params week_day: Week day from which want to retrieve the opening time.
    :params opening_hours: Opening hours of all the days.
    :returns: If the previous day have close time, returns the opening time.
    """

    inv_week_day_transitions = {v: k for k, v in WEEK_DAYS_TRANSITIONS.items()}
    prev_day = inv_week_day_transitions.get(week_day)
    prev_day_opening_hour = opening_hours.opening_hours.get(prev_day)

    if not prev_day_opening_hour:
        raise InvalidOpeningHoursException(f"No opening time for day: {prev_day}")

    opening_hour = prev_day_opening_hour[0]

    if opening_hour.type != OPEN:
        return None

    return opening_hour


def _validate_opening_and_closing_time(
    last_schedule_type_seen: str, schedule_type: str
) -> bool:
    """
    Validates if the schedule is correct.

    :params last_schedule_type_seen: Last schedule type seen (close/open)
    :params schedule_type: Schedule type (close/open)
    :returns: True if opening and closing time are valid, False in other case.
    """

    if not last_schedule_type_seen and schedule_type != OPEN:
        return False

    if last_schedule_type_seen == CLOSE and schedule_type != OPEN:
        return False

    if last_schedule_type_seen == OPEN and schedule_type != CLOSE:
        return False

    return True

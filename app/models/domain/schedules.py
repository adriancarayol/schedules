MONDAY = "monday"
TUESDAY = "tuesday"
WEDNESDAY = "wednesday"
THURSDAY = "thursday"
FRIDAY = "friday"
SATURDAY = "saturday"
SUNDAY = "sunday"

# Collection of available week days.
WEEK_DAYS = frozenset(
    (
        MONDAY,
        TUESDAY,
        WEDNESDAY,
        THURSDAY,
        FRIDAY,
        SATURDAY,
        SUNDAY,
    )
)

# Opening/closing time
OPEN = "open"
CLOSE = "close"
SCHEDULE_TYPES = frozenset(
    [
        OPEN,
        CLOSE,
    ]
)

# MIN/MAX value for seconds provided.
MIN_SECONDS_VALUE = 0
MAX_SECONDS_VALUE = 86399

# Available WEEK_DAYS_TRANSITIONS
# Useful to recover opening/closing time from next/prev days.
WEEK_DAYS_TRANSITIONS = {
    MONDAY: TUESDAY,
    TUESDAY: WEDNESDAY,
    WEDNESDAY: THURSDAY,
    THURSDAY: FRIDAY,
    FRIDAY: SATURDAY,
    SATURDAY: SUNDAY,
    SUNDAY: MONDAY,
}

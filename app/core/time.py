from datetime import datetime, timedelta


def humanize_seconds(seconds: int) -> str:
    """
    Takes a UNIX time in seconds and returns a human-readable string
    in %I:%M:%S %p format.
    For example, humanize_seconds(86399) will return 11:59:59 PM.

    :params seconds: Seconds to humanize
    :returns: Human-readable datetime string for the given time.
    """

    time = datetime(1970, 1, 1) + timedelta(seconds=seconds)
    return time.strftime("%I:%M:%S %p")

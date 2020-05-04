"""
农历日期
"""
import datetime

from typing import Tuple, Union

from calendar import monthrange

"""
国际常用
"""

DATETIME_PATTERN = "%Y-%m-%d %H:%M:%S"
DATE_PATTERN = "%Y-%m-%d"
TIME_PATTERN = "%H:%M:%S"

"""
中文常用
"""

WEEK_PREFIX = "周"
DATETIME_PATTERN_CHINESE = "%Y年%m月%d日%H时%M分%S秒"
DATE_PATTERN_CHINESE = "%Y年%m月%d日"
TIME_PATTERN_CHINESE = "%H时%M分%S秒"

DateType = datetime.date
DateTimeType = datetime.datetime
DateOrDateTimeType = Union[datetime.date, datetime.datetime]


def get_today():
    return datetime.date.today()


def get_date_by_day_offset(date, days) -> DateType:
    if not date:
        date = datetime.date.today()
    return date + datetime.timedelta(days=days)


def get_yesterday(date=None) -> DateType:
    if not date:
        date = datetime.date.today()
    return get_date_by_day_offset(date, days=-1)


def get_tomorrow(date=None) -> DateType:
    if not date:
        date = datetime.date.today()
    return get_date_by_day_offset(date, days=1)


def date_is_between(date_from: DateType, date: DateType, date_to: DateType) -> bool:
    return date_from < date < date_to


def get_week_start(date: DateType) -> DateType:
    start = date - datetime.timedelta(days=date.weekday())
    return start


def get_week_end(date: DateType) -> DateType:
    start = date - datetime.timedelta(days=date.weekday())
    end = start + datetime.timedelta(days=6)
    return end


def get_week_start_and_end(date: DateType) -> Tuple[DateType, DateType]:
    start = date - datetime.timedelta(days=date.weekday())
    end = start + datetime.timedelta(days=6)
    return start, end


def get_day_start(date: DateOrDateTimeType) -> DateTimeType:
    return datetime.datetime(date.year, date.month, date.day, 0, 0, 0)


def get_day_end(date: DateOrDateTimeType) -> DateTimeType:
    return datetime.datetime(date.year, date.month, date.day, 23, 59, 59)


def get_month_start(date: DateOrDateTimeType) -> DateTimeType:
    return datetime.datetime(date.year, date.month, 1, 0, 0, 0)


def get_month_end(date: DateOrDateTimeType) -> DateTimeType:
    return datetime.datetime(
        date.year, date.month, monthrange(date.year, date.month)[1], 23, 59, 59,
    )


def format_date(date, pattern=DATE_PATTERN) -> str:
    return datetime.datetime.strftime(date, pattern)


def format_datetime(dt, pattern=DATETIME_PATTERN) -> str:
    return datetime.datetime.strftime(dt, pattern)


def parse_date(date, pattern=DATE_PATTERN) -> datetime.date:
    return datetime.datetime.strptime(date, pattern)


def parse_datetime(dt, pattern=DATETIME_PATTERN) -> datetime.datetime:
    return datetime.datetime.strptime(dt, pattern)

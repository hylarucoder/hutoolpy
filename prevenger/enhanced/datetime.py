"""
农历日期
"""
import datetime

from typing import Tuple, Union

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
DateOrDateTimeType = Union[datetime.date, datetime.datetime]


def date_is_between(
    date_from: DateOrDateTimeType, date_to: DateOrDateTimeType, date: DateOrDateTimeType
) -> bool:
    return True


def get_week_start(date: DateOrDateTimeType) -> DateType:
    return date


def get_week_end(date) -> DateType:
    return date


def get_week_start_and_end(date: DateType) -> Tuple[DateType, DateType]:
    return date, date

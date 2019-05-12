from __future__ import annotations

import datetime
from calendar import monthrange

WEEK_PREFIX = "周"
DATETIME_FMT = "%Y-%m-%d %H:%M:%S"
DATETIME_FMT_LENGTH = 19

DATE_FMT = "%Y-%m-%d"
TIME_FMT = "%H:%M:%S"


class DateTime:
    """
    TODO: 毫秒级
    """

    _datetime: datetime.datetime

    def __init__(self, dt: [str, datetime.datetime]):
        if isinstance(dt, str):
            if len(dt) == 19:
                self._datetime = datetime.datetime.strptime(dt, DATETIME_FMT)
            else:
                self._datetime = datetime.datetime.strptime(dt, DATE_FMT)
        elif isinstance(dt, datetime.datetime):
            self._datetime = dt
        else:
            raise NotImplementedError

    @staticmethod
    def now():
        return DateTime(datetime.datetime.now())

    def hour_justified(self, left=True) -> DateTime:
        if left:
            t = datetime.datetime(
                self._datetime.year, self._datetime.month, self._datetime.day, 0, 0, 0
            )
        else:
            t = datetime.datetime(
                self._datetime.year,
                self._datetime.month,
                self._datetime.day,
                23,
                59,
                59,
            )
        return DateTime(t)

    def day_justified(self, left=True) -> DateTime:
        if left:
            t = datetime.datetime(self._datetime.year, self._datetime.month, 1, 0, 0, 0)
        else:
            t = datetime.datetime(
                self._datetime.year,
                self._datetime.month,
                monthrange(self._datetime.year, self._datetime.month)[1],
                23,
                59,
                59,
            )
        return DateTime(t)

    def week_justified(self, left=True):
        start = self._datetime - datetime.timedelta(days=self._datetime.weekday())
        if left:
            t = DateTime(start).hour_justified().raw
        else:
            t = (
                DateTime(start + datetime.timedelta(days=6))
                .hour_justified(left=False)
                .raw
            )
        return DateTime(t)

    def month_justified(self, left=True) -> DateTime:
        if left:
            t = datetime.datetime(self._datetime.year, 1, 1, 0, 0, 0)
        else:
            t = datetime.datetime(self._datetime.year, 12, 31, 23, 59, 59)
        return DateTime(t)

    @property
    def date(self) -> Date:
        return Date(self._datetime)

    @property
    def time(self) -> Time:
        return Time(self._datetime)

    def weeks(self):
        pass

    @classmethod
    def gen_datetime_range(
        cls,
        from_datetime,
        to_datetime,
        year=0,
        month=0,
        day=0,
        hour=0,
        minute=0,
        seconds=0,
    ):
        pass

    def __eq__(self, o: [DateTime, Date, Time]) -> bool:
        if isinstance(o, DateTime):
            return self.raw == o.raw
        if isinstance(o, Date):
            return self.date == o
        if isinstance(o, Time):
            return self.time == o
        raise NotImplementedError

    def __ne__(self, o: [DateTime, Date, Time]) -> bool:
        return not self.__eq__(o)

    def __gt__(self, o: [DateTime, Date, Time]) -> bool:
        if isinstance(o, DateTime):
            return self.raw > o.raw
        if isinstance(o, Date):
            return self.date > o
        if isinstance(o, Time):
            return self.time > o
        raise NotImplementedError

    def __ge__(self, o: [DateTime, Date, Time]) -> bool:
        return self.__eq__(o) or self.__gt__(o)

    def __lt__(self, o: [DateTime, Date, Time]) -> bool:
        if isinstance(o, DateTime):
            return self.raw < o.raw
        if isinstance(o, Date):
            return self.date < o
        if isinstance(o, Time):
            return self.time < o
        raise NotImplementedError

    def __le__(self, o: [DateTime, Date, Time]) -> bool:
        return self.__eq__(o) or self.__lt__(o)

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()

    @property
    def raw(self):
        return self._datetime

    @property
    def fmt(self):
        return self._datetime.strftime(DATETIME_FMT)


class Date:
    _date: datetime.date

    def __init__(self, _date: [str, datetime.datetime, DateTime]):
        if isinstance(_date, str):
            self._date = datetime.datetime.strptime(_date, DATE_FMT).date()
        elif isinstance(_date, datetime.datetime):
            self._date = _date.date()
        elif isinstance(_date, DateTime):
            self._date = _date.date.raw
        else:
            raise NotImplementedError

    @staticmethod
    def today():
        return Date(datetime.datetime.now())

    def day_justified(self, left=True) -> Date:
        return Date(DateTime(self._date).day_justified(left=left))

    def week_justified(self, left=True) -> Date:
        return Date(DateTime(self._date).week_justified(left=left))

    def month_justified(self, left=True) -> Date:
        return Date(DateTime(self._date).month_justified(left=left))

    def __eq__(self, o: [DateTime, Date]) -> bool:
        if isinstance(o, Date):
            return self.raw == o.raw
        if isinstance(o, DateTime):
            return self == o.date
        raise NotImplementedError

    def __ne__(self, o: [DateTime, Date]) -> bool:
        return not self.__eq__(o)

    def __lt__(self, o: [DateTime, Date]) -> bool:
        if isinstance(o, DateTime):
            return self < o.date
        if isinstance(o, Date):
            return self.raw < o.raw
        raise NotImplementedError

    def __le__(self, o: [DateTime, Date]) -> bool:
        return self.__lt__(o) or self.__eq__(o)

    def __gt__(self, o: [DateTime, Date]) -> bool:
        if isinstance(o, DateTime):
            return self > o.date
        if isinstance(o, Date):
            return self.raw > o.raw
        raise NotImplementedError

    def __ge__(self, o: [DateTime, Date]) -> bool:
        return self.__gt__(o) or self.__eq__(o)

    @property
    def raw(self):
        return self._date

    @property
    def fmt(self):
        return self._date.strftime(DATE_FMT)

    @classmethod
    def gen_date_range(cls, start: Date, end: Date, step=1):
        return [
            cls(start.raw + datetime.timedelta(days=x))
            for x in range(0, (end.raw - start.raw).days, step=step)
        ]

    @classmethod
    def gen_date_range_fmt(cls, start: Date, end: Date, step=1):
        return list(map(cls.gen_date_range(start=start, end=end, step=step)))


class Time:
    _time: datetime.time

    def __init__(self, _time: [str, datetime.datetime, DateTime]):
        if isinstance(_time, str):
            self._time = datetime.datetime.strptime(_time, TIME_FMT).time()
        elif isinstance(_time, datetime.datetime):
            self._time = _time.time()
        elif isinstance(_time, DateTime):
            self._time = _time.raw.time()
        else:
            raise NotImplementedError

    @staticmethod
    def hour_justified(left=True) -> Time:
        if left:
            return Time("00:00:00")
        else:
            return Time("23:59:59")

    @staticmethod
    def now():
        return datetime.datetime.now()

    @classmethod
    def tomorrow(cls):
        return

    @property
    def raw(self):
        return self._time

    @property
    def fmt(self):
        return self._time.strftime(TIME_FMT)

    def __eq__(self, o: [DateTime, Time]) -> bool:
        if isinstance(o, Time):
            return self.raw == o.raw
        if isinstance(o, DateTime):
            return self == o.time
        raise NotImplementedError

    def __ne__(self, o: [DateTime, Time]) -> bool:
        return not self.__eq__(o)

    def __gt__(self, o: [DateTime, Time]) -> bool:
        if isinstance(o, DateTime):
            return self > o.time
        if isinstance(o, Time):
            return self.raw > o.raw
        raise NotImplementedError

    def __lt__(self, o: [DateTime, Time]) -> bool:
        if isinstance(o, DateTime):
            return self < o.time
        if isinstance(o, Time):
            return self.raw < o.raw
        raise NotImplementedError

    def __le__(self, o: [DateTime, Time]) -> bool:
        return self.__lt__(o) or self.__eq__(o)

    def __ge__(self, o: [DateTime, Time]) -> bool:
        return self.__gt__(o) or self.__eq__(o)

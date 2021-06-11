import random
import string
import datetime
import uuid
from typing import Any

DEFAULT_RAN_LENGTH = 8


def rand_digits(length=DEFAULT_RAN_LENGTH):
    return "".join(random.choice(string.digits) for _ in range(length))


def rand_letters_digits(length=DEFAULT_RAN_LENGTH):
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


def rand_upper_ascii(length=DEFAULT_RAN_LENGTH):
    return "".join(random.choice(string.ascii_uppercase) for _ in range(length))


def rand_datetime(
    time_from: datetime.datetime, time_to: datetime.datetime
) -> datetime.datetime:
    random_timestamp = random.randint(time_from.timestamp(), time_to.timestamp())
    return datetime.datetime.fromtimestamp(random_timestamp)


def rand_date(date_from: datetime.date, date_to: datetime.date) -> datetime.date:
    def convert_date_to_datetime(date):
        return datetime.datetime.combine(date, datetime.datetime.min.time())

    return rand_datetime(
        convert_date_to_datetime(date_from), convert_date_to_datetime(date_to)
    ).date()


def rand_uuid():
    return str(uuid.uuid4())


class WeightedRand:
    total: int
    pairs: list[list[int, Any]]

    def __init__(self, pairs: list[list[int, Any]]):
        self.pairs = pairs
        self.total = sum(pair[0] for pair in pairs)

    def rand(self):
        r = random.randint(1, self.total)
        for (weight, value) in self.pairs:
            r -= weight
            if r <= 0:
                return value

import datetime
from prevenger.enhanced.random import (
    rand_digits,
    rand_letters_digits,
    DEFAULT_RAN_LENGTH,
    rand_upper_ascii,
    rand_datetime,
    rand_date,
    rand_uuid,
)


def test_rand_digits():
    assert len(rand_digits()) == DEFAULT_RAN_LENGTH


def test_rand_letters_digits():
    assert len(rand_letters_digits()) == DEFAULT_RAN_LENGTH


def test_rand_upper_ascii():
    assert len(rand_upper_ascii()) == DEFAULT_RAN_LENGTH


def test_rand_datetime():
    assert (
        rand_datetime(
            time_from=datetime.datetime(2018, 1, 1),
            time_to=datetime.datetime(2018, 12, 31),
        ).year
        == 2018
    )


def test_rand_date():
    assert (
        rand_date(
            date_from=datetime.datetime(2018, 1, 1),
            date_to=datetime.datetime(2018, 12, 31),
        ).year
        == 2018
    )


def test_rand_uuid():
    assert len(rand_uuid()) == 36

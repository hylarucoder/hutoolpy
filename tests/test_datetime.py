import datetime

from hutoolpy.datetime import (
    date_is_between,
    get_today,
    get_yesterday,
    get_tomorrow,
    get_week_start,
    get_week_end,
    get_week_start_and_end,
)


def test_get_today():
    assert datetime.date.today() == get_today()


def test_date_is_between():
    today = get_today()
    yesterday = get_yesterday()
    tomorrow = get_tomorrow()

    assert date_is_between(yesterday, today, tomorrow)


def test_get_week_start():
    date = get_today()
    start = date - datetime.timedelta(days=date.weekday())
    assert get_week_start(date) == start


def test_get_week_end():
    date = get_today()
    start = date - datetime.timedelta(days=date.weekday())
    end = start + datetime.timedelta(days=6)
    assert get_week_end(date) == end


def test_get_week_start_and_end():
    date = get_today()
    start = date - datetime.timedelta(days=date.weekday())
    end = start + datetime.timedelta(days=6)
    assert (start, end) == get_week_start_and_end(date)

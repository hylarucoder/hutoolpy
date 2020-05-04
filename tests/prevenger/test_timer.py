from prevenger.enhanced.datetime.timer import DateTime, Date, Time


def test_timer_datetime_parse_fmt():
    assert DateTime("2019-05-04") == DateTime("2019-05-04")
    assert DateTime("2019-05-04 00:00:00") == DateTime("2019-05-04")
    assert DateTime("2019-05-04 00:00:00") != DateTime("2019-05-04 00:00:01")

    assert DateTime("2019-05-04 00:00:00").time != DateTime("2019-05-04 00:00:01").time
    assert DateTime("2019-03-05 10:00:00").time == DateTime("2019-03-05 10:00:00").time

    assert DateTime("2019-05-04 00:00:00").date == DateTime("2019-05-04 00:00:01").date
    assert DateTime("2019-05-04 10:00:00").date != DateTime("2019-03-05 10:00:00").date

    assert DateTime("2019-05-04 10:00:00").fmt == "2019-05-04 10:00:00"


def test_timer_date_parse_fmt():
    assert Date("2019-05-04") == Date("2019-05-04")
    assert Date("2019-05-04").fmt == "2019-05-04"

    assert DateTime("2019-05-04 10:00:01") == Date("2019-05-04")


def test_timer_time_parse_fmt():
    assert Time("10:00:00") == Time("10:00:00")
    assert Time("10:00:01").fmt == "10:00:01"
    assert DateTime("2017-02-03 10:00:01") == Time("10:00:01")
    assert Time("10:00:00").hour_justified() == Time("00:00:00")
    assert Time("10:00:00").hour_justified(False) == Time("23:59:59")


def test_timer_justified():
    dt = DateTime("2019-05-04 20:30:00")
    assert dt.hour_justified() == DateTime("2019-05-04 00:00:00")
    assert dt.hour_justified(left=False) == DateTime("2019-05-04 23:59:59")
    assert dt.day_justified() == DateTime("2019-05-01 00:00:00")
    assert dt.day_justified(left=False) == DateTime("2019-05-31 23:59:59")
    assert dt.week_justified() == DateTime("2019-04-29 00:00:00")
    assert dt.week_justified(left=False) == DateTime("2019-05-05 23:59:59")
    assert dt.month_justified() == DateTime("2019-01-01 00:00:00")
    assert dt.month_justified(left=False) == DateTime("2019-12-31 23:59:59")

    dt = DateTime("2019-05-04 20:30:00")
    assert dt.hour_justified().day_justified().week_justified().month_justified() == DateTime(
        "2019-01-01 00:00:00"
    )


def test_timer_compare():
    assert DateTime("2017-02-03 10:00:01") >= DateTime("2017-02-03 10:00:00")
    assert DateTime("2017-02-03 10:00:01") >= DateTime("2017-02-03 10:00:01")
    assert DateTime("2017-02-03 10:00:01") > Date("2017-02-01")
    assert DateTime("2017-02-03 10:00:01") >= Date("2017-02-01")

    assert DateTime("2017-02-03 10:00:01") == Time("10:00:01")
    assert DateTime("2017-02-03 10:00:01") >= Time("10:00:01")
    assert DateTime("2017-02-03 10:00:03") >= Time("10:00:02")

    assert Time("10:00:01") < DateTime("2017-02-03 10:00:03") < Time("10:00:05")
    assert Time("10:00:01") <= DateTime("2017-02-03 10:00:01") <= Time("10:00:01")
    assert (
        DateTime("2017-02-03 10:00:01")
        <= Time("10:00:01")
        <= DateTime("2017-02-03 10:00:01")
    )
    assert (
        DateTime("2017-02-03 10:00:01")
        <= Time("10:00:03")
        <= DateTime("2017-02-03 10:00:05")
    )

    assert Date("2017-02-03") <= DateTime("2017-02-03 10:00:01") <= Date("2017-02-03")
    assert Date("2017-02-03") < DateTime("2017-02-04 10:00:01") < Date("2017-02-05")

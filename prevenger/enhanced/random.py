import random
import string

DEFAULT_RAN_LENGTH = 8


def rand_digits(length=DEFAULT_RAN_LENGTH):
    return "".join(random.choice(string.digits) for _ in range(length))


def rand_letters_digits(length=DEFAULT_RAN_LENGTH):
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


def rand_upper_ascii(length=DEFAULT_RAN_LENGTH):
    return "".join(random.choice(string.ascii_uppercase) for _ in range(length))


def rand_date():
    pass


def rand_datetime():
    pass

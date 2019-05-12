import random
import string


def rand_digits(length=8):
    return "".join(random.choice(string.digits) for _ in range(length))


def rand_letters_digits(length=8):
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


def rand_upper_ascii(length=8):
    return "".join(random.choice(string.ascii_uppercase) for _ in range(length))

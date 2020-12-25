import re


def has_pattern(_str, pattern):
    return bool(re.search(pattern, _str))


def is_pattern(_str, pattern):
    return bool(re.match(pattern, _str))


def sub_pattern(_str, pattern, sub):
    raise NotImplementedError()


def filter_pattern():
    raise NotImplementedError()


def find_first_matched_pattern(_str, pattern):
    arr = re.findall(pattern, _str)
    if len(arr) > 0:
        return arr[0]
    else:
        return None


def find_all_matched_pattern(_str, pattern):
    arr = re.findall(pattern, _str)
    if len(arr):
        return re.findall(pattern, _str)
    else:
        return None

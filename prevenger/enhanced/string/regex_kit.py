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


def is_blank():
    "字符串为 null 或者内部字符全部为 ' ' '\t' '\n' '\r' 这四类字符时返回 true"
    raise NotImplementedError


def not_blank():
    raise NotImplementedError


def snake_to_camel_case():
    raise NotImplementedError


def camel_to_snake_case():
    raise NotImplementedError


def capitalize(s: str):
    return s.capitalize()

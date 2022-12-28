import collections
import typing as T


def bulk_iter(func: T.Callable, iter: T.Iterable):
    raise NotImplementedError


def chunk_by(records: list, chunk_size=1000):
    """
    TODO: iter
    """
    return [records[x : x + chunk_size] for x in range(0, len(records), chunk_size)]


def find_duplicates(a: list):
    return [item for item, count in collections.Counter(a).items() if count > 1]


def remove_duplicates(seq: list):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

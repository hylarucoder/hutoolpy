import typing as T


def bulk_iter(func: T.Callable, iter: T.Iterable):
    raise NotImplementedError


def chunk_by(records: list, chunk_size=1000):
    """
    TODO: iter
    """
    return [records[x : x + chunk_size] for x in range(0, len(records), chunk_size)]

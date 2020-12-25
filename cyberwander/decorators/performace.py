from cProfile import Profile
import contextlib
import functools
import pstats
import time
from functools import wraps


def prof_deco(sort_by="cumtime", limit=10, timer=time.perf_counter):
    """
    参考了雨痕的 <Python学习笔记>
    :param sort_by:
    :param limit:
    :param timer:
    :return:
    """

    def decorator(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            p = Profile()
            p.enable()
            try:
                return func(*args, **kwargs)
            finally:
                p.disable()
                s = pstats.Stats(p).sort_stats(sort_by)
                s.print_stats(limit)

        return wrap

    return decorator


@contextlib.contextmanager
def prof_context(sort_by="cumtime", limit=10, timer=time.perf_counter):
    """
    参考了雨痕的 <Python学习笔记>
    :param sort_by:
    :param limit:
    :param timer:
    :return:
    """
    p = Profile()
    p.enable()
    try:
        yield
    finally:
        p.disable()
        s = pstats.Stats(p).sort_stats(sort_by)
        s.print_stats(limit)

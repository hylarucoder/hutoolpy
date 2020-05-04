from cProfile import Profile
import contextlib
import functools
import pstats
import time
from functools import wraps


def timethis(func):
    """
    Decorator that reports the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        func_name = func.__name__
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        msg = "{func_name} :\t 耗时 {last_sec}".format(
            func_name=func_name, last_sec=(end - start)
        )
        # TODO: 以后有机会引入日志系统,现在先用打印将就着
        print(msg)
        return result

    return wrapper


# http://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p13_making_stopwatch_timer.html
class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError("Already started")
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError("Not started")
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()


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

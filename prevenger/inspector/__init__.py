import inspect


def get_function_args(f):
    return inspect.getfullargspec(f)[0]

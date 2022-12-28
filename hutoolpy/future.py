from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


def within_flask(fn):
    from flask import current_app

    app_context = current_app.app_context()

    def wrapper(*args, **kwargs):
        with app_context:
            return fn(*args, **kwargs)

    return wrapper


def multi_thread_submit(
    func,
    items,
    max_workers=10,
):
    executor = ThreadPoolExecutor(max_workers=max_workers)
    future_list = []
    for item in items:
        future_list.append(executor.submit(func, *item["args"], **item["kwargs"]))  # .add_done_callback()
    done_iter = as_completed(future_list)
    executor.shutdown(wait=True)
    return done_iter


def multi_process_submit(
    func,
    items,
    max_workers=10,
):
    executor = ProcessPoolExecutor(max_workers=max_workers)

    future_list = []
    for item in items:
        future_list.append(executor.submit(func, *item["args"], **item["kwargs"]))  # .add_done_callback()
    done_iter = as_completed(future_list)
    executor.shutdown(wait=True)
    return done_iter

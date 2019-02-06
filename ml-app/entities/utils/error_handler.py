from functools import wraps


def handle_errors(func):
    @wraps(func)
    def wrap_over_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            raise error
    return wrap_over_func

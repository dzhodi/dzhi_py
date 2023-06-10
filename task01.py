"""In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use raw_input() instead

    >>> f()
    ? 1
    '1'
    >>> f()     # will remember previous value
    '1'
    >>> f()     # but use it up to two times only
    '1'
    >>> f()
    ? 2
    '2'
"""
from functools import wraps


def cache(times):
    def decorator(func):
        history = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal history
            for i, (args_cached, kwargs_cached, result) in enumerate(history):
                if args == args_cached and kwargs == kwargs_cached:
                    if i >= len(history) - times:
                        return result
                    else:
                        del history[i]
                        break
            result = func(*args, **kwargs)
            history.append((args, kwargs, result))
            return result

        return wrapper

    return decorator

"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    # Defining an empty dictionary that will hold the cached results
    cached_results = {}

    # Defining the function that will do the work of caching the results
    def caching_func(*args):
        # If the arguments passed to the function are already cached, the cached result is returned
        if args in cached_results:
            return cached_results[args]
        # Otherwise, the original function is called, the result is stored in the cache, and it is returned
        result = func(*args)
        cached_results[args] = result
        return result

    # Returning the function that does the caching
    return caching_func


# Defining the original function for which we will create a caching function
def func(a, b):
    return (a + b) * 2


# Using the cache function to create a caching version of the function func
cache_func = cache(func)

# Making the function call with a pair of arguments
some = (100, 200)
val_1 = cache_func(*some)
val_2 = cache_func(*some)

# Checking that the cached result is the same as the original one
assert val_1 is val_2

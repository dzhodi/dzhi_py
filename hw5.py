"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(iterable, start, stop=None, step=1):
    try:
        # Check if the iterable is unique
        if len(iterable) != len(set(iterable)):
            raise ValueError("Iterable must contain unique values")

        # Get the index of the starting value
        start_index = iterable.index(start)

        # If stop is not provided, set it to the end of the iterable
        if stop is None:
            stop_index = len(iterable)
        else:
            stop_index = iterable.index(stop)

        # Create a list of values within the range
        result = []
        for i in range(start_index, stop_index, step):
            result.append(iterable[i])

        return result
    except ValueError as e:
        # Log the error
        print(f"Error: {e}")

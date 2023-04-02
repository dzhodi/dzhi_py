"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    i = 3
    while i >= len(data):
        if len(data) < 3 or data[0] == 1 and data[0] == 0 or data[1] == 1 and data[1] == 0:
            return False
        if data[i - 2] + data[i - 3] != data[i-1]:
            return False
        else:
            return True


check_fibonacci([21, 34, 54])

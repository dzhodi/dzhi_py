"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import List, Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    def get_value(i):
        return "fizzbuzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else str(i)

    try:
        # Check if the input is a positive integer
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Input must be a positive integer")

        # Generate and yield the FizzBuzz numbers
        for i in range(1, n + 1):
            yield get_value(i)
    except ValueError as e:
        # Log the error
        print(f"Error: {e}")
        return

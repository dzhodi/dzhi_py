"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    try:
        # Check if input is a list
        if not isinstance(inp, list):
            raise TypeError("Input must be a list")

        n = len(inp)
        freq = {}

        # Count the frequency of each element in the input list
        for i in inp:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        # Find the most common element
        most_common = max(freq, key=freq.get)

        # Find the least common element
        least_common = min(freq, key=freq.get)

        # Return the tuple of most common and least common elements
        return most_common, least_common
    except TypeError as e:
        # Log the error
        print(f"Error: {e}")
        return 0, 0

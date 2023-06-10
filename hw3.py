"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""

from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:
    # Check if only one list is provided - return a list of lists with each element of the input list
    if len(args) == 1:
        return [[item] for item in args[0]]
    else:
        result = []
        # Get all combinations from the remaining lists except for the first one (via recursive call)
        rest = combinations(*args[1:])
        for item in args[0]:  # Loop through all elements of the first list
            for elements in rest:  # Loop through all combinations of remaining lists
                result.append([item] + elements)  # Add a new combination to the list
        return result

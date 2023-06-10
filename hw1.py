"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    count = 0
    for value in tree.values():
        if isinstance(value, dict):
            count += find_occurrences(value, element)
        elif isinstance(value, (list, tuple)):
            for item in value:
                if isinstance(item, dict):
                    count += find_occurrences(item, element)
                elif item == element:
                    count += 1
        elif value == element:
            count += 1
    return count


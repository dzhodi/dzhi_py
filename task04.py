"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
import itertools


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    sums = (itertools.product(a, b, c, d))
    res = int(0)
    for el in sums:
        if sum(el) == 0:
            res += 1
    return res


print(check_sum_of_four([-8, 8, 3, 5], [7, -3, -2, -9], [2, 1, 0, -9], [0, 4, 5, 2]))

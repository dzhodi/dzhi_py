"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import heapq
from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    # Open all files and create a list of iterators
    iterators = [open(file, "r") for file in file_list]
    # Merge the iterators using heapq.merge()
    merged_iterator = heapq.merge(*iterators)
    # Yield each integer from the merged iterator
    yield from (int(line) for line in merged_iterator)
    # Close all files
    for iterator in iterators:
        iterator.close()

"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
import collections


def get_longest_diverse_words(file_path: str) -> List[str]:
    mass = []
    with open(file_path, encoding="unicode-escape") as f:
        data = f.read()
        data1 = re.findall(r"[\w']+|[!#$%&'()*+,-./:;<=>?@[]^_`{|}~" "]", data)
        c = 1
        for i in data1:
            if len(set(i)) >= len(set(data1[c])):
                mass.append(i)
            c += 1
            if c == len(data1):
                break
    return sorted(mass, key=lambda w: len(w), reverse=True)[:10]


def get_rarest_char(file_path: str) -> str:
    with open(file_path, encoding="unicode-escape") as f:
        data = f.read()
        data = list(data.replace(" ", ""))
        ch = collections.Counter(data)
        red = [k for k, v in ch.items() if v == min(ch.values())]
    return "".join(red)


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode-escape") as f:
        data = f.read()
        count = 0
        for char in data:
            if char in string.punctuation:
                count += 1
    return count


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode-escape") as f:
        data = f.read()
        count = 0
        for char in data:
            if ord(char) > 127:
                count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, encoding="unicode-escape") as f:
        data = f.read()
        non_ascii_chars = [char for char in data if ord(char) > 127]
        if not non_ascii_chars:
            return ""
        return collections.Counter(non_ascii_chars).most_common(1)[0][0]

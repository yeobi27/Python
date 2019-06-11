from typing import Any


def linear_search(lst: list, value: Any) -> int:

    lst.append(value)

    i = 0

    while lst[i] != value:
        i = i+1

    lst.pop()

    if i == len(lst):
        return -1
    else:
        return i

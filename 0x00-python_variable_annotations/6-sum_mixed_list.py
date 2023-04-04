#!/usr/bin/env python3
"""Defines a function that sums up a list."""


def sum_mixed_list(mxd_lst: int | float) -> float:
    """Function that returns the sum of a mixed list."""
    total = 0
    for i in range(len(mxd_lst)):
        total += mxd_lst[i]
    return total

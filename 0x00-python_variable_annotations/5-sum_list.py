#!/usr/bin/env python3
"""Defines a function that sums a list"""


def sum_list(input_list: float) -> float:
    """Function that returns the sum of a list of float values"""
    sum = 0
    for i in range(len(input_list)):
        sum += input_list[i]
    return sum

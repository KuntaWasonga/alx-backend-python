#!/usr/bin/env python3
"""Defines a floor function."""


def floor(n: float) -> int:
    """Function that returns the floor oF n."""
    if (n >= 0):
        return int(n)
    else:
        return int(n) - 1

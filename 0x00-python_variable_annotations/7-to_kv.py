#!/usr/bin/env python3
"""Defines a tuple function."""


def to_kv(k: str, v: int | float) -> tuple[str, int]:
    """Function that creates a tuple from 2 elements."""
    list = [k, v]
    mytuple = tuple(list)
    return mytuple

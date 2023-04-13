#!/usr/bin/env python3
"""Defines a tuple function."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function that creates a tuple from 2 elements."""
    return (k, float(v**2))

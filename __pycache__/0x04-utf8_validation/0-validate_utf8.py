#!/usr/bin/python3
"""_summary_
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """a function that validates an
    array of integers against utf-8

    Args:
        data (List[int]): list of
        integers to be validated

    Returns:
        bool: true if valid utf-8 else false
    """
    try:
        bytes(data).decode()
    except BaseException:
        return False
    return True

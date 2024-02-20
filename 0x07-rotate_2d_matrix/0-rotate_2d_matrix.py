#!/usr/bin/python3
""" typing method for type hinting"""

from typing import List, Any


def rotate_2d_matrix(matrix: List[List[Any]]) -> None:
    """function that rotates a 2d array clockwise

    Args:
        matrix (List[List[Any]]): a 2d array to be rotated
    """
    size = len(matrix)
    for i in range(size):
        for j in range(i, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()

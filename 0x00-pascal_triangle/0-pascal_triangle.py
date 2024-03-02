#!/usr/bin/python3
"""Pascals triangle implemntation"""


def pascal_triangle(n):
    """Returns an aray of arrays representing the pascal_triangle"""
    pascals_array = []
    for i in range(n):
        temp_array = []
        if pascals_array:
            temp_array.append(1)
            j = 0
            r = 1
            while j < (len(pascals_array[i - 1]) - 1):
                value = pascals_array[i - 1][j] + pascals_array[i - 1][r]
                j = r
                r += 1
                temp_array.append(value)
        temp_array.append(1)
        pascals_array.append(temp_array)
    return pascals_array

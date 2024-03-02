#!/usr/bin/python3
"""This module provides access to some
objects used or maintained by the
interpreter and to functions that
interact strongly with the interpreter
"""
import sys


def throne(queen, column, prev_data):
    """_summary_

    Args:
        queen (_type_): _description_
        column (_type_): _description_
        prev_data (_type_): _description_

    Returns:
        _type_: _description_
    """
    available = []
    for array_list in prev_data:
        for x in range(column):
            if is_safe(queen, x, array_list):
                available.append(array_list + [x])
    return available


def assemble(row, column):
    """_summary_

    Args:
        row (_type_): _description_
        column (_type_): _description_

    Returns:
        _type_: _description_
    """
    solution = [[]]
    for queen in range(row):
        solution = throne(queen, column, solution)
    return solution


def is_safe(q, x, array_list):
    """_summary_

    Args:
        q (_type_): _description_
        x (_type_): _description_
        array_list (_type_): _description_

    Returns:
        _type_: _description_
    """
    if x in array_list:
        return False
    else:
        return all(
                abs(
                    array_list[column] - x
                    ) != q - column for column in range(q)
                )


def validate_input():
    """_summary_

    Returns:
        _type_: _description_
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    """_summary_"""
    n = validate_input()
    solutions = assemble(n, n)
    for array_list in solutions:
        clean = []
        for q, x in enumerate(array_list):
            clean.append([q, x])
        print(clean)


if __name__ == "__main__":
    n_queens()

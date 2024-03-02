#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """a method that calculates the
    fewest number of operations needed
    to result in exactly n H characters
    in the file

    Args:
        n (int): maximum number of H to paste

    Returns:
        int: total number of operations
        done on a file
    """
    copy = "H"
    paste = "H"
    operations = 0

    for _ in range(0, n):
        if n % len(paste):
            if len(paste) == n:
                break
            paste += copy
            operations += 1
        else:
            if len(paste) == n:
                break
            copy = paste
            operations += 1
            paste += copy
            operations += 1
    return operations

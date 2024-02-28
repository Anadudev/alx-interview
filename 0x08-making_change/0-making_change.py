#!/usr/bin/python3
""" find the minimum number of coins required to make up
a given total amount, given a list of coin denominations"""


def makeChange(coins, total):
    """function that calculates

    Args:
        coins (_type_): list of in integers
        total (_type_): total coins to be gotten

    Returns:
        int: minimum number og addition to get total or -1 on error
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    i = 0
    getter = coins[i]
    calc = 0
    while i < len(coins):
        if getter == total:
            return calc + 1
        if coins[i] <= 0:
            return -1
        if getter < total:
            getter += coins[i]
            calc += 1
        if getter > total:
            getter -= coins[i]
            calc -= 1
            i += 1
    return -1

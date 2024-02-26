#!/usr/bin/python3
""" find the minimum number of coins required to make up
a given total amount, given a list of coin denominations"""


def handler(coins, total, index=0, ballance=0, tracker=1):
    """handler function that calculates the fewest number
        of addition to get a total coin

    Args:
        coins (List[int]): list representing coins
        total (int): represents target value
        index (int, optional): tracks position in coins. Defaults to 0.
        ballance (int, optional): tracks total gotten coins. Defaults to 0.
        tracker (int, optional): tracks total additions. Defaults to 1.

    Returns:
        _type_: _description_
    """
    if ballance > total:
        ballance -= coins[index]
        tracker -= 1
        index += 1
    elif ballance < total:
        ballance += coins[index]
        tracker += 1
    elif ballance == total:
        return tracker
    return handler(coins, total, index, ballance, tracker)


def makeChange(coins, total) -> int:
    """function that calculates

    Args:
        coins (_type_): list of in integers
        total (_type_): total coins to be gotten

    Returns:
        int: minimum number og addition to get total or -1 on error
    """
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    for i, j in enumerate(coins):
        if j <= total:
            break
    try:
        return handler(coins[i:], total, 0, coins[i])
    except IndexError:
        return -1

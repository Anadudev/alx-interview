#!/usr/bin/python3
""" Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from the
set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally, determine
who the winner of each game is.

Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
Example:

x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for Maria to choose """


def isWinner(x, nums):
    """Determines the winner of a game between Maria and Ben based on the
    number of rounds and a set of consecutive integers.

    The game involves choosing prime numbers from a set of consecutive integers
    starting from 1 up to and including n. Players take turns to choose a prime
    number and remove that number and its multiples from the set. The player who
    cannot make a move loses the game.

    Args:
        x (int): The number of rounds in the game.
        nums (List[int]): A list of integers representing the set for the game.

    Returns:
        str: The name of the player that won the most rounds. If the winner cannot
        be determined, returns None.

    Example:
        >>> isWinner(3, [4, 5, 1])
        'Maria'

    Note:
        - The function assumes that Maria always goes first and both players play optimally.
        - The function does not import any packages and is designed to work with n and
        x not larger than 10000."""
    if not nums or x < 1:
        return None
    max_num = max(nums)

    my_filter = [True for _ in range(max(max_num + 1, 2))]

    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not my_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            my_filter[j] = False
    my_filter[0] = my_filter[1] = False

    y = 0

    for i, _ in enumerate(my_filter):
        if my_filter[i]:
            y += 1
        my_filter[i] = y

    player1 = 0

    for x in nums:
        player1 += my_filter[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"

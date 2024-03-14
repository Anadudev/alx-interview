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


def get_multiples(x, nums):
    """_summary_

    Args:
        x (_type_): _description_
        nums (_type_): _description_
    """
    n = max(nums) + 1
    multiple = [i * x for i in range(1, n)]
    for i in nums:
        if i in multiple:
            nums.remove(i)
    # return nums


def isPrime(num):
    """_summary_

    Args:
        num (_type_): _description_

    Returns:
        _type_: _description_
    """
    if num <= 1:
        return False
    for x in range(num):
        if x <= 1:
            continue
        if num % x == 0:
            return False
    return True


def isWinner(x, nums):
    """_summary_

    Args:
        x (_type_): _description_
        nums (_type_): _description_

    Returns:
        _type_: _description_
    """
    players = ["maria", "ben"]
    n = 1
    nums.sort()
    for _ in range(x):
        if len(nums) == 1 and nums[0] == 1:
            break
        n = 0 if n > 0 else 1
        for num in nums:
            if isPrime(num):
                get_multiples(num, nums)
    return players[n]

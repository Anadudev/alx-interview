#!/usr/bin/python3

canUnlockAll = __import__("0-lockboxes").canUnlockAll

boxes = [[1], [2], [3], [4], [12]]
print(canUnlockAll(boxes), "True")

boxes = [[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]
print(canUnlockAll(boxes), "True")

boxes = [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes), "False")

boxes = [[0]]
print(canUnlockAll(boxes), "True")

boxes = "12 boxes with random keys"
print(boxes)

boxes = "1000 boxes with all keys in each box"
print(boxes)

boxes = [
    [10, 3, 8, 9, 6, 5, 8, 1],#10,3,8
    [8, 5, 3, 7, 1, 8, 6],
    [5, 1, 9, 1],#5
    [],
    [6, 6, 9, 4, 3, 2, 3, 8, 5],#2
    [9, 4],#9,4
    [4, 2, 5, 1, 1, 6, 4, 5, 6],#4
    [9, 5, 8, 8],
    [6, 2, 8, 6],#6
]
print(canUnlockAll(boxes), "True")

boxes = [
    [7, 5],
    [1, 10, 7],
    [9, 6, 10],
    [7, 9],
    [2],
    [7, 3],
    [7, 9, 10, 10, 8, 9, 2, 5],
    [7, 2, 2, 4, 4, 2, 4, 8, 7],
    [4, 2, 9, 6, 6, 5, 5],
]
print(canUnlockAll(boxes), "False")

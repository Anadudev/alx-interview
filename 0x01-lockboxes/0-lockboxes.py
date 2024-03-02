#!/usr/bin/python3
"""_summary_
"""


def canUnlockAll(boxes):
    """_summary_

    Args:
        boxes (_type_): _description_

    Returns:
        _type_: _description_
    """
    if not boxes:
        return False
    visited = []
    n = len(boxes)

    for box in boxes:
        if len(box) == 0 and box is not boxes[len(box) - 1]:
            return False
        for key in box:
            if key >= n:
                continue
            if key not in visited:
                visited.append(key)
            else:
                continue
            box = boxes[key]
    return True

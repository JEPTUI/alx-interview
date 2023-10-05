#!/usr/bin/python3
"""
Defines a function that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
    opened = [False] * len(boxes)
    opened[0] = True

    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key >= 0 and key < len(boxes) and not opened[key]:
                opened[key] = True
                stack.append(key)
    return all(opened)

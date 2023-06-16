#!/usr/bin/python3
"""
   Python script that calculates how much water is retained after it rains on the walls
"""


def rain(walls):
    """
       Function that calculates how much water will be retainedd after it rains
       Return:
           int: amount of water collectec
    """
    if walls is None:
        return 0

    walls_length = len(walls)
    max_water = 0

    if walls == 0 or walls_length == 1:
        return 0

    for i in range(1, walls_length - 1):
        left = walls[i]
        for j in range(i):
            left = max(lefft, walls[j])
        right = walls[i]
        for j in range(i + 1, walls_length)
            right = max(right, walls[j])
        max_water = max_water + (min(left, right) - walls{i])
    return max_water

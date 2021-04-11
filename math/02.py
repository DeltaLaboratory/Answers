"""
create at 2021-04-11
Author Demi-Ad
두 점에 거리 구하기
"""

import math


def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    a = x1 - x2
    b = y1 - y2
    return math.sqrt((a * a) + (b * b))


print(distance(4, 2, 2, 1))

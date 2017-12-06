import math
from collections import deque

## Part 1
def spiral_distance(n):
    if n == 1: return 0
    square = math.ceil(pow(n, 0.5))
    if (square % 2 == 0):
        square = square + 1

    a = pow(square, 2) - math.floor(square / 2)
    b = a - square + 1
    c = b - square + 1
    d = c - square + 1

    seg_1 = min([abs(x - n) for x in [a, b, c, d]])
    seg_2 = math.floor(square / 2)
    return(seg_1 + seg_2)

## Part 2
def build_spiral(n):
    # right, up, left, down
    order = deque([[1, 0], [0, 1], [-1, 0], [0, -1]])

    i, j = 0, 1
    x = y = 0
    out = [[x, y, 1]]

    while(True):
        for _ in range(2):
            direction = order.popleft()
            order.append(direction)
            dx, dy = direction
            for _ in range(j):
                x, y = x + dx, y + dy
                val = sum([z for x1, y1, z in out if adjacent(x, y, x1, y1)])
                if val > n:
                    return val
                out.append([x, y, val])
                i = i + 1
        j = j + 1

def adjacent(x1, y1, x2, y2):
    return((abs(x1 - x2) <= 1) and (abs(y1 - y2) <= 1))

import numpy as np


def burst(pos, facing, grid, count):
    y, x = pos
    if grid[y][x]:
        grid[y][x] = 0
        facing = turn(facing, "r")
    else:
        grid[y][x] = 1
        facing = turn(facing, "l")
        count += 1

    dy, dx = facing
    pos = [y + dy, x + dx]

    return pos, facing, grid, count


def burst2(pos, facing, grid, count):
    # 0 = clean, 1 = infected, 2 = weakened, 3 = flagged
    y, x = pos
    if grid[y][x] == 0:
        grid[y][x] = 2
        facing = turn(facing, "l")

    elif grid[y][x] == 2:
        grid[y][x] = 1
        count += 1

    elif grid[y][x] == 1:
        grid[y][x] = 3
        facing = turn(facing, "r")

    elif grid[y][x] == 3:
        grid[y][x] = 0
        facing = reverse(facing)

    dy, dx = facing
    pos = [y + dy, x + dx]

    return pos, facing, grid, count


def turn(facing, direction):
    clockwise = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    i = clockwise.index(facing)

    if direction == "r":
        i = (i + 1) % 4
    else:
        i = i - 1 if i > 0 else 3

    return clockwise[i]


def reverse(facing):
    dy, dx = facing
    return [-dy, -dx]


def simulate(n, fun, lines):
    size = 1000
    count = 0
    center = size // 2
    pos = [center - 1, center - 1]
    facing = [-1, 0]

    grid = np.zeros([size, size], dtype=int)
    grid[center - len(lines)/2: center + len(lines) / 2,
         center - len(lines)/2: center + len(lines) / 2] += lines

    for i in range(n):
        pos, facing, grid, count = fun(pos, facing, grid, count)

    return count


def main(input_file):
    lines = []
    with open(input_file) as f:
        for line in f.readlines():
            line = line.replace("#", '1')
            line = line.replace(".", '0')
            lines.append([int(i) for i in line.strip()])

    part1 = simulate(10000, burst, lines)
    part2 = simulate(10000000, burst2, lines)

    return {"part1": part1, "part2": part2}

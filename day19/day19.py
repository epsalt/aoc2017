from string import ascii_uppercase

def walk_path(dat):
    y = 0
    x = dat[0].index("|")
    letters = []
    dy, dx = 1, 0
    steps = 0

    while(True):
        val = dat[y][x]

        if val in ascii_uppercase:
            letters.append(val)

        if val == " ":
            break
        elif val == "+":
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            directions.remove([-dy, -dx])
            for test in directions:
                ty, tx = test
                try:
                    tval = dat[y + ty][x + tx]
                    if (tval != " "):
                        dy, dx = ty, tx
                except IndexError:
                    pass

        y, x = y + dy, x + dx
        steps += 1

    return letters, steps

def main(input_file):
    with open(input_file) as f:
        lines = [line.rstrip('\r\n') for line in f.readlines()]

    dat = []
    for line in lines:
        l = []
        for char in line:
            l.append(char)
        dat.append(l)

    letters, steps = walk_path(dat)
    letters = "".join(letters)

    return {"part1": letters, "part2": steps}

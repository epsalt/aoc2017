def io(INPUT):
    with open(INPUT) as f:
        return [int(line.strip()) for line in f.readlines()]

def jump(arr, part2=False):
    pos = step = 0

    while(True):
        try:
            jump = arr[pos]
            if part2 and jump >= 3:
                arr[pos] = arr[pos] - 1
            else:
                arr[pos] = arr[pos] + 1
            pos = pos + jump
            step = step + 1

        except IndexError:
            return step

def main(INPUT):
    print("Part 1: {}".format(jump(io(INPUT))))
    print("Part 2: {}".format(jump(io(INPUT), part2 = True)))

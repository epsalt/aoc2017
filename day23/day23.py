from collections import defaultdict

def coprocessor(lines):
    ops = {"set": lambda x, y: y,
           "sub": lambda x, y: x - y,
           "mul": lambda x, y: x * y}

    regs = defaultdict(int)
    i = 0
    count = 0

    while i < len(lines):
        op, var, val = lines[i]

        if op == "mul":
            count += 1

        try:
            val = int(val)
        except ValueError:
            val = regs[val]

        if ops.get(op):
            fun = ops.get(op)
            regs[var] = fun(regs[var], val)
            i += 1

        else:
            try:
                x = int(var)
            except ValueError:
                x = regs[var]

            if x != 0:
                i += val
            else:
                i += 1

    return count

def part2():
    b = 81 * 100 + 100000
    c = b + 17000
    h = 0

    for i in range(b, c + 1, 17):
        for j in range(2, i):
            if i % j == 0:
                h += 1
                break

    return h

def main(input_file):
    with open(input_file) as f:
        lines = [line.strip().split(" ") for line in f.readlines()]

    return {"part1": coprocessor(lines), "part2": part2()}

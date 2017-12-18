
def spinlock(spins, n):
    l = [0]
    pos = 0

    for i in range(1, n + 1):
        pos = 1 + (pos + spins) % len(l)
        l.insert(pos, i)

    return (l, pos)

def spinlock2(spins, n):
    pos = 0
    for i in range(1, n + 1):
        pos = 1 + (pos + spins) % i
        if pos == 1:
            out = i
    return out

def main(n):
    l, pos = spinlock(n, 2017)
    part2 = spinlock2(n, 50000000)

    return {"part1": l[pos+1], "part2": part2}

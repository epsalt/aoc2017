def generator(seed, b, c, d, n):
    i = 0
    val = seed
    while i < n:
        val = (val * b) % c
        if (val % d == 0):
            yield val
            i += 1

def judge(a, b):
    a = '{0:b}'.format(a)[-16:]
    b = '{0:b}'.format(b)[-16:]

    return a == b

def loop(a_seed, b_seed, d1, d2, n):
    a = generator(a_seed, 16807, 2147483647, d1, n)
    b = generator(b_seed, 48271, 2147483647, d2, n)
    tally = 0

    for i in range(n-1):
        if judge(next(a), next(b)):
            tally += 1
        else:
            pass
    return tally

def main(a_seed, b_seed):
    part1 = loop(a_seed, b_seed, 1, 1, 40000000)
    part2 = loop(a_seed, b_seed, 4, 8,  5000000)

    return({"part1": part1, "part2": part2})

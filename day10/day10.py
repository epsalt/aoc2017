from functools import reduce

def knot_hash(lengths, n_marks, rounds):
    pos = skip = 0
    l = list(range(n_marks))

    for _ in range(rounds):
        for length in lengths:
            seq = [(pos + i) % n_marks for i in range(length)]
            temp = l[::]
            for i, j in zip(seq, seq[::-1]):
                l[i] = temp[j]

            pos = pos + length + skip
            skip = skip + 1

    return l

def full_knot_hash(lengths, n_marks, rounds, chunk_size):
    lengths = [ord(s) for s in lengths] + [17, 31, 73, 47, 23]
    sparse_hash = knot_hash(lengths, n_marks, rounds)

    chunks = [reduce(lambda x,y: x ^ y, sparse_hash[i:i+chunk_size])
              for i in range(0, len(sparse_hash), chunk_size)]

    out = []
    for chunk in chunks:
        h = hex(chunk)[2:]
        if(len(h) < 2):
            h = '0' + h
        out.append(h)
    return ''.join(out)

def main(INPUT):
    single = knot_hash([int(s.strip()) for s in INPUT.split(',')], 256, 1)
    part1 = single[0] * single[1]
    full = full_knot_hash(INPUT, 256, 64, 16)

    return {"part1": part1, "part2": full}

def memory(arr):
    out = [arr[:]]
    count = 1

    while(True):
        max_val = max(arr)
        i_max = arr.index(max_val)

        arr[i_max] = 0
        for i in cycle(i_max, len(arr), max_val):
            arr[i] = arr[i] + 1
        if arr in out:
            return {"part1": count, "part2": count - out.index(arr)}
        else:
            out.append(arr[:])
            count = count + 1

def cycle(start, size, n):
    loc = start
    for i in range(n):
        if loc + 1 == size:
            loc = 0
        else:
            loc = loc + 1
        yield(loc)

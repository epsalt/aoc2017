def parse(input_file):
    out = {}
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            key, value = map(int, line.split(":"))
            out[key] = value
    return out

def run(scanners, delay):
    severity = 0
    caught = False
    for depth in scanners.keys():
        rng = scanners[depth]
        if (delay + depth) % (2 * rng - 2) == 0:
            caught = True
            severity += depth * rng

    return severity, caught

def main(input_file):
    scanners = parse(input_file)
    severity, _ = run(scanners, 0)
    delay = 0

    while(True):
        _, caught = run(scanners, delay)
        if caught:
            delay = delay + 1
        else:
            break

    return {"part1": severity, "part2": delay}

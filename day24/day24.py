from copy import deepcopy

def build_bridges(bridge, components, l = []):
    if not bridge:
        tail = 0
    else:
        tail = bridge[-1][-1]

    matches = [c for c in components if tail in c]

    if not matches:
        l.append(bridge)
        return bridge

    else:
        for match in matches:
            c = deepcopy(components)
            b = deepcopy(bridge)

            c.remove(match)
            if match[0] == tail:
                b.append(match)
            else:
                b.append([match[1], match[0]])
            build_bridges(b, c)

    return l

def main(input_file):
    with open(input_file) as f:
        components = [list(map(int, line.strip().split("/")))
            for line in f.readlines()]

    bridges = build_bridges([], components)
    max_strength = max([strength(bridge) for bridge in bridges])
    max_length = max([len(bridge) for bridge in bridges])
    strongest_max_length = max([strength(bridge) for bridge in bridges if len(bridge) == max_length])

    return {"part1": max_strength, "part2": strongest_max_length}

def strength(bridge):
    return sum([sum(i) for i in bridge])

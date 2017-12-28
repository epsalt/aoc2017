from collections import defaultdict

blueprint =  {"a": [[1, +1, "b"], [0, -1, "c"]],
              "b": [[1, -1, "a"], [1, +1, "c"]],
              "c": [[1, +1, "a"], [0, -1, "d"]],
              "d": [[1, -1, "e"], [1, -1, "c"]],
              "e": [[1, +1, "f"], [1, +1, "a"]],
              "f": [[1, +1, "a"], [1, +1, "e"]]}

def main(blueprint):
    tape = defaultdict(lambda: 0)
    state = 'a'
    steps = 12134527
    pos = 0

    for i in range(steps):
        out, delta, state = blueprint[state][tape[pos]]
        tape[pos] = out
        pos = pos + delta

    return {"part1": sum(tape.values())}

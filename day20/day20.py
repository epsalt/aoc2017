import copy
import re

def parse(line):
    m = re.findall(r"\<([0-9,-]+)\>", line)
    p, v, a = map(lambda x: [int(k) for k in x.split(",")], m)

    return [p, v, a]

def step(particle):
    particle[1][0] += particle[2][0]
    particle[1][1] += particle[2][1]
    particle[1][2] += particle[2][2]

    particle[0][0] += particle[1][0]
    particle[0][1] += particle[1][1]
    particle[0][2] += particle[1][2]

    return particle

def dist_from_origin(particle):
    return abs(particle[0][0]) + abs(particle[0][1]) + abs(particle[0][2])

def main(input_file):
    with open(input_file) as f:
        particles = [parse(line.strip()) for line in f.readlines()]

    collisions = copy.deepcopy(particles)

    for _ in range(1000):
        for i in range(len(particles)):
            particles[i] = step(particles[i])

    for _ in range(100):
        for i in range(len(collisions)):
            collisions[i] = step(collisions[i])

        removes = []
        for particle in collisions:
            c = [p for p in collisions if p[0] == particle[0]]
            if len(c) > 1:
                for p in c:
                    removes.append(p)
        for r in removes:
            try: collisions.remove(r)
            except ValueError:
                pass

    dists = [dist_from_origin(particle) for particle in particles]
    closest = dists.index(min(dists))

    return {"part1": closest, "part2": len(collisions)}

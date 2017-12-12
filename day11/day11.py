# Thanks to https://www.redblobgames.com/grids/hexagons/

class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def move(self, direction):
        dir_map = {'n' : Cube( 0,  1, -1),
                   'ne': Cube( 1,  0, -1),
                   'se': Cube( 1, -1,  0),
                   's' : Cube( 0, -1,  1),
                   'sw': Cube(-1,  0,  1),
                   'nw': Cube(-1,  1,  0)}

        offset = dir_map[direction]

        return Cube(self.x + offset.x,
                    self.y + offset.y,
                    self.z + offset.z)

def distance(a, b):
    return int((abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)) / 2)

def main(s):
    directions = s.split(",")
    origin = position = Cube(0, 0, 0)
    current_distance = max_distance = 0

    for direction in directions:
        position = position.move(direction)
        current_distance = distance(position, origin)
        if current_distance > max_distance:
            max_distance = current_distance

    return {"part1": current_distance, "part2": max_distance}

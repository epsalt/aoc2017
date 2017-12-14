def defragment(s, grid_size):
    out = []
    for i in range(grid_size):
        s_index = ("{}-{}".format(s,i))

        ## full_knot_hash from day 10
        knot_hash = full_knot_hash(s_index, 256, 64, 16)
        binary = bin(int(knot_hash, base=16))[2:].zfill(128)
        out.append(binary)
    return(out)

class Cell:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.marked = (val == '0')
        self.neighbours = []

    def set_neighbours(self, cells):
        potential_neighbours = [[self.x + 1, self.y    ],
                                [self.x - 1, self.y    ],
                                [self.x    , self.y + 1],
                                [self.x    , self.y - 1]]

        for potential in potential_neighbours:
            x, y = potential
            if (-1 < x < 128) and (-1 < y < 128):
                try:
                    self.neighbours.append(cells[x][y])
                except IndexError:
                    pass
            else:
                pass

def populate_cells(grid):
    cells = []
    for x, line in enumerate(grid):
        l = []
        for y, val in enumerate(line):
            l.append(Cell(x, y, val))
        cells.append(l)

    for line in cells:
        for cell in line:
            cell.set_neighbours(cells)

    return(cells)

def visit(cell):
    if cell.marked:
        return None
    cell.marked = True
    for neighbour in cell.neighbours:
        visit(neighbour)

def main(s):
    grid = defragment(s, 128)

    ones = zeroes = regions =  0
    for line in grid:
        for char in line:
            if char == '1': ones += 1
            else: zeroes += 1

    cells = populate_cells(grid)
    for line in cells:
        for cell in line:
            if cell.marked:
                pass
            else:
                visit(cell)
                regions += 1

    return {"part1": ones, "part2": regions}

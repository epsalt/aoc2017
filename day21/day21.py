import numpy as np

def parse(line):
    line = line.replace('#', '1')
    line = line.replace('.', '0')
    return [np.array([list(i) for i in k.split('/')]).astype(int) for k in line.split(' => ')]

def alt_forms(square):
    rot90 = np.rot90(square)
    rot180 = np.rot90(rot90)
    rot270 = np.rot90(rot180)

    forms = [square, rot90, rot180, rot270]
    out = []
    for f in forms:
        out.append(np.flipud(f))
        out.append(np.fliplr(f))

    return out + forms

def fractal(input_file, iters):
    with open(input_file) as f:
        lines = [parse(a.strip()) for a in f.readlines()]

    artbook = {}
    for line in lines:
        i, o = line
        alts = alt_forms(i)
        for form in alts:
            artbook[form.data.tobytes()] = o

    current = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

    for i in range(iters):
        size = current.shape[0]

        if  size % 2 == 0: n = 2
        else: n = 3

        hs = np.array([])
        for h in np.hsplit(current, size / n):
            vs = np.array([])
            for v in np.vsplit(h, size / n):
                section = artbook[v.tobytes()]
                vs = np.concatenate((vs, section), 0) if vs.size else section
            hs = np.concatenate((hs, vs), 1) if hs.size else vs

        current = hs

    return(np.count_nonzero(current))

def main(input_file):
    print({'part1': fractal(input_file, 5), 'part2': fractal(input_file, 18)})

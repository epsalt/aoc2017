from string import ascii_lowercase

class Dancers:
    def __init__(self, line):
        self.line = line
        self.n = len(self.line)

    def spin(self, x):
        self.line = self.line[-x:] + self.line[:self.n - x]

    def exchange(self, a, b):
        self.line[a], self.line[b] = self.line[b], self.line[a]

    def partner(self, a, b):
        self.exchange(self.line.index(a), self.line.index(b))

    def __str__(self):
        return ''.join(self.line)

def main(in_file):

    with open(in_file) as f:
        data = f.read().strip()
    instructions = data.split(',')

    dancers = Dancers(list(ascii_lowercase[:16]))
    results = [str(dancers)]

    while(True):
        start = str(dancers)
        for s in instructions:
            if s[0] == 's':
                dancers.spin(int(s[1:]))
            elif s[0] == 'x':
                a, b = map(int, s[1:].split("/"))
                dancers.exchange(a, b)
            else:
                dancers.partner(s[1], s[3])

        if str(dancers) in results:
            break
        else:
            results.append(str(dancers))

    pos = int(1E9 % len(results))

    return {"part1": results[1], "part2": results[pos]}

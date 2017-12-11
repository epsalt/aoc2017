class Stream:
    def __init__(self, initialState):
        self.currentState = initialState
        self.score = 0
        self.total = 0
        self.garbage_count = 0

    def runAll(self, inputs):
        inputs = iter(list(inputs))
        for i in inputs:
            if i == "!":
                inputs.__next__()
                continue

            if self.currentState.valid:
                if i == "{":
                    self.score = self.score + 1
                if i == "}":
                    self.total = self.total + self.score
                    self.score = self.score - 1

            if not self.currentState.valid and I != ">":
                self.garbage_count = self.garbage_count + 1

            self.currentState = self.currentState.next(i)

        return self.total, self.garbage_count

class Group:
    def __init__(self):
        self.valid = True

    def next(self, input):
        if input == "<": return Stream.garbage
        else: return Stream.group

class Garbage:
    def __init__(self):
        self.valid = False

    def next(self, input):
        if input == ">": return Stream.group
        else: return Stream.garbage

Stream.group = Group()
Stream.garbage = Garbage()

def main(INPUT):
    stream = Stream(Stream.group)
    part1, part2 = stream.runAll(INPUT)
    return({"part1": part1, "part2": part2})

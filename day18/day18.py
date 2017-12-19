from collections import defaultdict, deque

def duet(lines):
    ops = {"set": lambda x, y: y,
           "add": lambda x, y: x + y,
           "mul": lambda x, y: x * y,
           "mod": lambda x, y: x % y, }

    regs = defaultdict(int)
    i = sound = 0
    while i < len(lines):

        split = lines[i].split(" ")

        if len(split) == 3:
            op, var, val = split
            try:
                val = int(val)
            except ValueError:
                val = regs[val]
        else: op, var = split

        if ops.get(op):
            fun = ops.get(op)
            regs[var] = fun(regs[var], val)

        elif op == "snd":
            sound = regs[var]

        elif op == "rcv":
            if regs[var] != 0:
                return sound

        elif op == "jgz":
            if regs[var] > 0:
                i += val
                continue

        i += 1

def duet2(lines, i, regs, msg_in):
    ops = {"set": lambda x, y: y,
           "add": lambda x, y: x + y,
           "mul": lambda x, y: x * y,
           "mod": lambda x, y: x % y, }

    split = lines[i].split(" ")

    if len(split) == 3:
        op, var, val = split
        try: val = int(val)
        except: val = regs[val]
    else:
        op, var = split

    waiting = False
    msg_out = None

    if ops.get(op):
        fun = ops.get(op)
        regs[var] = fun(regs[var], val)
        i += 1
        return i, regs, msg_out, waiting

    elif op == "jgz":
        try: x = int(var)
        except: x = regs[var]
        if x > 0:
            i += val
        else:
            i += 1

        return i, regs, msg_out, waiting

    elif op == "snd":
        try: msg_out = int(var)
        except: msg_out = int(regs[var])
        i += 1
        return i, regs, msg_out, waiting

    elif op == "rcv":
        if msg_in is not None:
            regs[var] = msg_in
            i += 1
            return i, regs, msg_out, waiting
        else:
            waiting = True
            return i, regs, msg_out, waiting

    else:
        raise LookupError

def main(in_file):
    with open(in_file) as f:
        lines = [line.strip() for line in f.readlines()]

    regs0 = defaultdict(int)
    regs1 = defaultdict(int)

    regs0['p'] = 0
    regs1['p'] = 1

    inbox0 = deque()
    inbox1 = deque()

    i0 = i1 = count = 0
    msg_in0 = msg_in1 = None
    waiting0 = waiting1 = False

    while(True):

        if waiting0:
            try: msg_in0 = inbox0.popleft()
            except: msg_in0 = None
        else:
            msg_in0 = None

        if waiting1:
            try: msg_in1 = inbox1.popleft()
            except: msg_in1 = None
        else:
            msg_in1 = None

        i0, regs0, msg_out0, waiting0 = duet2(lines, i0, regs0, msg_in0)
        i1, regs1, msg_out1, waiting1 = duet2(lines, i1, regs1, msg_in1)

        if msg_out0 is not None:
            inbox1.append(msg_out0)
            msg_out0 = None
        if msg_out1 is not None:
            count = count + 1
            inbox0.append(msg_out1)
            msg_out1 = None

        if waiting0 and waiting1 and (not inbox0) and (not inbox1):
            break

    return {"part1": duet(lines), "part2": count}

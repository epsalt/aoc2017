def parse(s, d):
    var1, operation, val1, _, var2, operator, val2 = s.split(" ")

    lookup = {"inc": "+", "dec": "-"}
    operation = lookup[operation]

    # Initialize
    for var in var1, var2:
        if var not in d:
            d[var] = 0

    template = "if(d['{}'] {} {}): d['{}'] = d['{}'] {} {}"
    obj = template.format(var2, operator, val2, var1, var1, operation, val1)

    exec(obj)
    return(d)

def main(INPUT):
    with open(INPUT) as f:
        lines = [line.strip() for line in f.readlines()]

    global_max = 0
    d = dict()
    for line in lines:
        d = parse(line, d)
        current_max = max(value for key, value in d.items())
        if current_max > global_max:
            global_max = current_max

    return({"part1": current_max, "part2": global_max})

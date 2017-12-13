from functools import reduce

def build_graph(INPUT):
    with open(INPUT) as f:
        lines = [line.strip() for line in f]

    out = {}
    for line in lines:
        parent, children = line.split(" <-> ")
        children = list(map(int, children.split(", ")))
        out[int(parent)] = children

    return out

def find_path(graph, start, end, path=[]):
    """Copied from https://www.python.org/doc/essays/graphs/"""
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def membership_size(graph, node):
    size = 0
    for key, values, in graph.items():
        if find_path(graph, key, node) is not None:
            size = size + 1
    return size

def build_sets(graph):
    sets = []
    for key, values in graph.items():
        current_set = set(values).union(set([key]))
        sets.append(set(frozenset(current_set)))
    return sets

def merge(sets, fset):
    if not sets:
        return [fset]
    
    out = []
    found_intersect = False
    
    for s in sets:
        if fset.intersection(s):
            found_intersect = True
            out.append(s.union(fset))
        else:
            out.append(s)
            
    if not found_intersect:
        out.append(fset)

    return out

def count_groups(sets):
    count = None
    
    while(True):
        sets = reduce(lambda x,y: merge(x,y), [[]] + sets)
        new_count = len(sets)
        if new_count == count:
            return count
        else:
            count = new_count
        
def main(INPUT):
    graph = build_graph(INPUT)
    size = membership_size(graph, 0)

    sets = build_sets(graph)
    count = count_groups(sets)

    return {"part1": size, "part2": count}

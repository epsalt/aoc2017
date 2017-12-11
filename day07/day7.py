import re

def parse(INPUT):
    programs = dict()
    relationships = list()
    with open(INPUT) as f:
        lines = [line.strip() for line in f.readlines()]

        for line in lines:
            parent = re.search(r'^([\w\-]+)', line).group()
            weight = re.search(r'\d+', line).group()
            programs[parent] = Node(parent, weight)

            children = re.search(r'(?<=-> ).*', line)
            if children:
                children = [child.strip() for child in children.group().split(",")]
                for child in children:
                    relationships.append([child, parent])

        return(programs, relationships)

class Node(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = None

    def add_child(self, obj):
        self.children.append(obj)

    def add_parent(self, obj):
        self.parent = obj

def build_tree(nodes, relationships):
    for rel in relationships:
        child, parent = rel
        nodes[parent].add_child(nodes[child])
        nodes[child].add_parent(nodes[parent])
    return(nodes)

def total_weight(node):
    if not node.children:
        return(int(node.weight))
    else:
        return(int(node.weight) + sum([total_weight(child) for child in node.children]))

def balanced(node):
    if not node.children:
        return True
    else:
        child_weights = [total_weight(child) for child in node.children]
        return(len(set(child_weights)) == 1)

def part1(INPUT):
    nodes, rels = parse(INPUT)
    tree = build_tree(nodes, rels)
    for _, node in tree.items():
        if not node.parent:
            return(node.name)

def part2(INPUT):
    nodes, rels = parse(INPUT)
    tree = build_tree(nodes, rels)
    for _, node in tree.items():
        if not balanced(node) and all([balanced(child) for child in node.children]):
            total_weights= [total_weight(child) for child in node.children]
            good_weight = max(set(total_weights), key=total_weights.count)
            outlier = min(set(total_weights), key=total_weights.count)

            for child in node.children:
                if total_weight(child) == outlier:
                    return int(child.weight) + (good_weight - outlier)

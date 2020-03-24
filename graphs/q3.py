import math

class Btree:
    root = None

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def list_of_depths(tree):
    root = tree.root
    levels = {}
    _helper(levels, 1, root)
    return levels

def _helper(levels, level, node):
    if node == None:
        return
    if not level in levels:
        levels[level] = []

    levels[level].append(node.val)
    _helper(levels, level + 1, node.left)
    _helper(levels, level + 1, node.right)




def minimal_tree(values):
    num_values = len(values)
    if num_values == 0:
        return None
    if num_values == 1:
        return Node(values[0])

    min_height = int(math.ceil(math.log2(num_values + 1)))
    mid = 2 ** (min_height - 1) - 1
    left = minimal_tree(values[:mid])
    right = minimal_tree(values[mid+1:])
    return Node(values[mid], left, right)

t = Btree()
t.root = minimal_tree(range(20))
d = list_of_depths(t)
print(d)
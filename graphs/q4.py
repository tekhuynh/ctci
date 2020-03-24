import math

class Btree:
    root = None

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def balanced(tree):
    root = tree.root
    left = height(1, root.left)
    right = height(1, root.right)
    if abs(left - right) > 1:
        return False
    return True

def height(level, node):
    if node == None:
        return level - 1
    return max(height(level + 1, node.left), height(level + 1, node.right))

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
print(balanced(t))
t.root = Node(1, Node(1, Node(1)))
print(balanced(t))
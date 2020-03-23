import math

class BTree:
    def __init__(self, root = None):
        self.root = root
    def print(self):
        self.print_node(self.root)
    def height(self):
        return self._height(1, self.root)
    def _height(self, level, node):
        if node == None:
            return level - 1
        return max(self._height(level + 1, node.left),self._height(level+1, node.right))
    def print_node(self, node):
        if node == None:
            return
        print(str(node.val))
        self.print_node(node.left)
        self.print_node(node.right)

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

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
    
tree = BTree()
print(tree.height())
print("")

for i in [2 ** x - 1 for x in range(5)]:
    print("x = %d" % (i))
    tree.root = minimal_tree(range(i))
    print(tree.height())
    print("")
    tree.print()
    print("")
for i in [2 ** x for x in range(5)]:
    print("x = %d" % (i))
    tree.root = minimal_tree(range(i))
    print(tree.height())
    print("")
    tree.print()
    print("")
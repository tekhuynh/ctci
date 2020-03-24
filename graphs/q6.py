import math

class Node:
    def __init__(self, val, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def successor(node):
    if node == None:
        return None

    if node.right == None and node.parent == None:
        return None

    if node.right == None:
        currnode = node
        while currnode != None and currnode.val > currnode.parent.val:
            currnode = currnode.parent

        if currnode == None:
            return None
        return currnode.parent
    
    currnode = node.right
    while currnode.left != None:
        currnode = currnode.left
    return currnode


def minimal_tree(values):
    num_values = len(values)
    if num_values == 0:
        return None
    if num_values == 1:
        return Node(values[0])

    min_height = int(math.ceil(math.log2(num_values + 1)))
    mid = 2 ** (min_height - 1) - 1
    curr = Node(values[mid])
    curr.left = minimal_tree(values[:mid])
    curr.left.parent = curr
    curr.right = minimal_tree(values[mid+1:])
    curr.right.parent = curr
    return curr

n = minimal_tree(range(15))
a = n.left.right.right
s = successor(a)
print(a.val, s.val)
a = n.left.right.left
s = successor(a)
print(a.val, s.val)
a = n.left.right
s = successor(a)
print(a.val, s.val)
a = n
s = successor(a)
print(a.val, s.val)
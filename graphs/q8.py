import math

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def common_ancestor(root, val1, val2):
    if root == None:
        return None, False

    left, lflag = common_ancestor(root.left, val1, val2)
    if lflag:
        return left, True
    right, rflag = common_ancestor(root.right, val1, val2)
    if rflag:
        return right, True

    if left != None and right != None:
        return root, True

    if root.val == val1 or root.val == val2:
        if left == None and right == None:
            return root, False
        else:
            return root, True
    
    if left == None:
        return right, False
    else:
        return left, False


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

node, found = common_ancestor(n, 1, 12)
print(node.val, found)
node, found = common_ancestor(n, 0, 2)
print(node.val, found)
node, found = common_ancestor(n, 0, 1)
print(node.val, found)
node, found = common_ancestor(n, 16, 12)
print(node.val, found)
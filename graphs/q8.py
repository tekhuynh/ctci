import math

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def common_ancestor(root, val1, val2):
    if root == None:
        return None
    if root.val == val1:
        return root
    if root.val == val2:
        return root

    left = common_ancestor(root.left, val1, val2)
    if left != None and left.val != val1 and left.val != val2:
        return left
    right = common_ancestor(root.right, val1, val2)
    if right != None and right.val != val1 and right.val != val2:
        return right
    
    if left == None:
        return right
    if right == None:
        return left
    
    return root


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

print(common_ancestor(n, 1, 12).val)
print(common_ancestor(n, 0, 2).val)

import math

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def is_bst(node):
    if node == None:
        return True
    if node.left == None and node.right == None:
        return True
    
    if node.left != None and node.left.val >= node.val:
        return False
    if node.right != None and node.val >= node.right.val:
        return False
    
    return is_bst(node.left) and is_bst(node.right)



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

print(is_bst(minimal_tree(range(20))))
print(is_bst(minimal_tree(range(20)[::-1])))
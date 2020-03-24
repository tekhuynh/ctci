
import math

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def is_bst(node):
    if node == None:
        return True, None, None
    if node.left == None and node.right == None:
        return True, node.val, node.val
    
    isbst = False
    leftisbst, leftmin, leftmax = is_bst(node.left)
    rightisbst, rightmin, rightmax = is_bst(node.right)

    if not leftisbst and rightisbst:
        return False, 0, 0
    if leftmax != None and leftmax > node.val:
        return False, 0, 0
    if rightmin != None and rightmin < node.val:
        return False, 0, 0
    
    if leftmin == None:
        leftmin = node.val
    if rightmax == None:
        rightmax = node.val

    return True, leftmin, rightmax



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
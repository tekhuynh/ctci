
def successor(node):
    if node == None:
        return None
    if node.parent == None:
        return None
    if node.parent.val > node.val:
        return parent
    if node.parent.right.val > node.val:
        return parent.right
    return successor(parent)
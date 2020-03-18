class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 

def kth(k, headnode):
    if headnode == None:
        return None
    if k <= 1:
        return headnode
    return kth(k-1, headnode.next)

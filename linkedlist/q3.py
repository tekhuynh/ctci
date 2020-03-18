class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_node(n):
    n.val = n.next.val
    n.next = n.next.next

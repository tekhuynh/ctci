class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_dup(headnode):
    buf = set()
    curr = headnode
    prev = None
    while (curr != None):
        if curr.val in buf:
            prev.next = curr.next
        else:
            buf.add(curr.val)
        prev = curr
        curr = curr.next

def no_buf(headnode):
    curr = headnode
    while curr != None:
        remove_val(curr, curr.val)
        curr = curr.next

def remove_val(headnode, val):
    if headnode == None:
        return
    if headnode.next == None:
        return
    if headnode.next.val == val:
        headnode.next = headnode.next.next
    remove_val(headnode.next, val)
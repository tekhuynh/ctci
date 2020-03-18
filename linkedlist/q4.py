class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def part(n, ll):
    if ll.head.next == None:
        return

    pivot = None
    prev = None
    curr = ll.head
    while curr != None:
        if curr.val >= n:
            if prev == None:
                ll.head = curr.next
                curr.next = pivot
                pivot = curr
                curr = ll.head
            else:
                prev.next = curr.next
                curr.next = pivot
                pivot = curr
                curr = prev.next
        else:
            prev = curr
            curr = curr.next
    if prev == None:
        ll.head = pivot
    else:
        prev.next = pivot
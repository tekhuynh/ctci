class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = None

class LinkedList:
    head = None

def add(l1, l2):
    n1 = getNum(l1)
    n2 = getNum(l2)
    digits = [int(i) for i in str(n1 + n2)]

    sumlist = LinkedList()
    for d in digits:
        n = Node(d, sumlist.head)
        sumlist.head = n

    return sumlist

def addrev(l1, l2):
    n1 = getNumRev(l1)
    n2 = getNumRev(l2)
    digits = [int(i) for i in str(n1 + n2)]

    sumlist = LinkedList()
    for d in digits[::-1]:
        n = Node(d, sumlist.head)
        sumlist.head = n

    return sumlist

def getNum(ll):
    node = ll.head
    res = 0
    mult = 1
    while node != None:
        res += node.val * mult
        mult *= 10
        node = node.next
    return res

def getNumRev(ll):
    node = ll.head
    res = 0
    while node != None:
        res = node.val + res * 10
        node = node.next
    return res
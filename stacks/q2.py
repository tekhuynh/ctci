class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class SLinkedList:
    head = None

class Stack:
    def __init__(self):
        self.ll = SLinkedList()
        self.min = SLinkedList()
    def push(self, val):
        self.ll.head = Node(val, self.ll.head)
        if self.min.head == None or self.min.head.val <= val:
            self.min.head = Node(val, self.min.head)
    def pop(self, val):
        n = self.ll.head
        if n != None:
            self.ll.head = self.ll.head.next
            if n.val == self.min.head.val:
                self.min.head = self.min.head.next
        return n.val
    def mini(self):
        return self.min.head.val

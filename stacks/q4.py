class Stack:
    def __init__(self):
        self.list = list()
    def pop(self):
        if not self.list:
            return None
        return self.list.pop()
    def push(self, val):
        self.list.append(val)
    def peek(self):
        if not self.list:
            return None
        return self.list[-1]

class Queue:
    def __init__(self):
        self.old = Stack()
        self.new = Stack()
    def enqueue(self, val):
        self.new.push(val)
    def dequeue(self):
        if self.old.peek() == None:
            while self.new.peek() != None:
                self.old.push(self.new.pop())
        return self.old.pop()
    def print(self):
        print(self.old.list)
        print(self.new.list)

a = Queue()
[a.enqueue(i) for i in range(10)]
print(a.dequeue())
a.print()
class Stack:
    def __init__(self):
        self.list = list()
    def push(self, val):
        self.list.append(val)
    def pop(self):
        if not self.list:
            return None
        return self.list.pop()
    def peek(self):
        if not self.list:
            return None
        return self.list[-1]

class SortedStack:
    def __init__(self):
        self.stack = Stack()
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack.peek()
    def isEmpty(self):
        return self.stack.peek() == None
    def push(self, val):
        if self.stack.peek() == None:
            self.stack.push(val)
            return
        temp = Stack()
        while self.stack.peek() != None:
            if val >= self.stack.peek():
                break
            temp.push(self.stack.pop())
        self.stack.push(val)
        while temp.peek() != None:
            self.stack.push(temp.pop())
    def print(self):
        print(self.stack.list)


a = SortedStack()
[a.push(i) for i in range(1, 10, 2)]
a.print()
[a.push(i) for i in range(2, 10, 2)[::-1]]
a.print()

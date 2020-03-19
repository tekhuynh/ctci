class Stack:
    def __init__(self):
        self.list = list()
        self.items = 0
    def push(self, val):
        self.list.append(val)
        self.items += 1
    def pop(self):
        if self.items == 0:
            return None
        self.items -= 1
        return self.list.pop()
    def peek(self):
        if self.items == 0:
            return None
        return self.list[-1]


class SetOfStacks:
    def __init__(self, thresh):
        self.stack = Stack()
        self.thresh = thresh
    def push(self, val):
        top = self.stack.peek()
        if top == None or top.items == self.thresh:
            top = Stack()
            self.stack.push(top)
        top.push(val)
    def pop(self):
        top = self.stack.peek()
        if top == None:
            return None
        item = top.pop()
        if top.items == 0:
            self.stack.pop()
        return item
    def popAt(self, i):
        if i >= self.stack.items:
            return None
        return self.stack.list[i].pop()
    def print(self):
        for i in self.stack.list:
            print(" ".join([str(j) for j in i.list]))

a = SetOfStacks(5)
[a.push(i) for i in range(50)]
print(a.popAt(2))
a.print()
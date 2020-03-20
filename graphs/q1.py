class Graph:
    def __init__(self):
        self.dict = dict()
    def add_node(self, _id):
        if _id in self.dict:
            return False
        self.dict[_id] = list()
        return True
    def add_edge(self, _from, _to):
        if _from == _to:
            return False
        if not _from in self.dict and _to in self.dict:
            return False
        self.dict[_from].append(_to)
        return True
    def has_edge(self, _from, _to):
        if _to in self.dict[_from]:
            return True
        return False
    def get_edges(self, _id):
        return self.dict[_id]

class Queue:
    def __init__(self):
        self.list = list()
    def add(self, items):
        if type(items) is list:
            self.list += items
        else:
            self.list.append(items)
    def pop(self):
        if not self.list:
            return None
        return self.list.pop(0)
    def is_empty(self):
        if self.list:
            return False
        return True

def route(graph, a, b):
    visited = set()
    queue = Queue()
    queue.add(a)
    while not queue.is_empty():
        currnode = queue.pop()
        if currnode in visited:
            continue
        if g.has_edge(currnode, b):
            return True
        queue.add(graph.get_edges(currnode))
        visited.add(currnode)

    return False

g = Graph()
[g.add_node(i) for i in range(10)]
[g.add_edge(0, i) for i in range(1, 3)]
[g.add_edge(2, i) for i in range(3, 7)]
print(route(g, 0, 9))
[g.add_edge(6, i) for i in range(7, 10)]
print(route(g, 0, 9))

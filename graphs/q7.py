import collections

def build_order(projects, dependencies):
    p = set(projects)
    d = set(dependencies)
    order = []
    while p:
        dependent = set([x[1] for x in d])
        independent = p.difference(dependent)
        if not independent:
            return None
        order += list(independent)
        [p.remove(i) for i in independent]
        remove = [i for i in d if i[0] in independent]
        [d.remove(i) for i in remove]
    return order

print(build_order(['a', 'b', 'c', 'd', 'e', 'f'], [('a','d'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d','c')]))
print(build_order(['a', 'b', 'c', 'd', 'e', 'f'], [('a','d'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d','c'), ('c', 'a')]))

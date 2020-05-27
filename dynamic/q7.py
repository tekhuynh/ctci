def combinations(n):
    for i in range(1 << n):
        index = 0
        indexes = []
        while i > 0:
            if i & 1 == 1:
                indexes.append(index)
            index += 1
            i >>= 1
        yield indexes

def permutations(a):
    if a == []:
        yield []
    for i in a:
        ii = [x for x in a if x != i]
        for j in permutations(ii):
            yield [i] + j

for i in permutations("abcd"):
    print(i)
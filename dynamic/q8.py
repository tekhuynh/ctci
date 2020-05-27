def comb(n):
    for i in range(1 << n):
        index = 0
        indexes = []
        while i > 0:
            if i & 1 == 1:
                indexes.append(index)
            index += 1
            i >>= 1
        yield indexes

def perm(arr):
    if arr == []:
        yield []
    for i in arr:
        ii = [x for x in arr if x != i]
        for j in perm(ii):
            yield [i] + j

def permdup(arr):
    d = dict()
    for i in arr:
        if not i in d:
            d[i] = 0
        d[i] += 1
    return permdup2(d)

def permdup2(d):
    if len(d) == 0:
        yield []
    for k in d:
        dd = d.copy()
        dd[k] -= 1
        if dd[k] == 0:
            del dd[k]
        for j in permdup2(dd):
            yield [k] + j

for i in permdup("abbccc"):
    print(i)
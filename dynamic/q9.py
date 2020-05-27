def parens(n):
    return parens2(n, n)

def parens2(o, c):
    if o == 0:
        yield ")" * c
        return
    for i in parens2(o - 1, c):
        yield "(" + i
    if c > o:
        for i in parens2(o, c - 1):
            yield ")" + i

res = []
for i in parens(8):
    print(i)
    res.append(i)
print(len(res), len(set(res)))
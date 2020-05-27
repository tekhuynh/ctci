def subsets(a):
    length = len(a)
    num_subsets = 1 << length
    res = []
    for i in range(num_subsets):
        res.append(convert(a, i))
    return res

def convert(a, k):
    subset = []
    index = 0
    while k > 0:
        if k & 1 == 1:
            subset.append(a[index])
        k >>= 1
        index += 1
    return subset

print(subsets([1,2,3,4]))
import math

def q3(a):
    return q3h(a, 0, len(a))

def q3h(a, start, end):
    if start == end:
        return None

    mid = int((start + end)/2)
    print(mid, a[mid])

    if a[mid] == mid:
        return mid
    
    if a[mid] < mid:
        return q3h(a, mid+1, end)
    
    return q3h(a, start, mid)

a = [(i - 8) *2 for i in range(20)]
b = [i for i in range(20)]
print(q3(a))
print(b)
print(a)
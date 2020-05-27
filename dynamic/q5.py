def multiply(a, b):
    small = min(a,b)
    big = max(a,b)

    if small == 0:
        return 0

    res = 0
    shifts = 0
    while small > 0:
        if small & 1 == 1:
            res += big << shifts
        small >>= 1
        shifts += 1

    return res

print(multiply(12, 12))
print(multiply(12, 11))
print(multiply(120000000000000000000000, 120000000000000000000000))
def palperm(s):
    chars = s.lower().replace(' ', '')

    m = {}

    for c in chars:
        if c in m:
            m[c] += 1
        else:
            m[c] = 1

    num_odd = 0
    for v in m.values():
        if v % 2 == 1:
            num_odd += 1
    if num_odd > 1:
        return False
    return True


s = input()
print(palperm(s))
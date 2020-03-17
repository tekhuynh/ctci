def edits(s1, s2):
    s1len = len(s1)
    s2len = len(s2)

    diff = s1len-s2len
    if abs(diff) > 1:
        return False

    s1ptr = 0
    s2ptr = 0
    edits = 0
    while s1ptr < s1len and s2ptr < s2len:
        if s1[s1ptr] == s2[s2ptr]:
            s1ptr += 1
            s2ptr += 1
            continue

        edits += 1

        if diff == 0:
            s1ptr += 1
            s2ptr += 1
        elif diff < 0:
            s2ptr += 1
        else:
            s1ptr += 1
    
    if edits <= 1:
        return True
    else:
        return False

s1 = input()
s2 = input()
print(edits(s1,s2))
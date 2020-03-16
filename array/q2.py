def is_perm(s1, s2):
    s1 = list(s1)
    s1.sort()
    s2 = list(s2)
    s2.sort()
    if not len(s1) == len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

s1 = input()
s2 = input()
print(is_perm(s1,s2))
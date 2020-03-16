def is_unique(s):
    chars = list(s)
    chars.sort()
    for i in range(len(s)-1):
        if chars[i] == chars[i+1]:
            return False
    return True

s = input()
print(is_unique(s))




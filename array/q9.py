def isSubstring(sub, string):
    return sub in string

def isRot(s1, s2):
    if len(s1) != len(s2):
        return False
    if isSubstring(s1, s2 * 2):
        return True
    return False


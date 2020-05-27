def count_eval(exp, res):
    counts = count_eval2(exp)
    if res == False:
        return counts[0]
    if res == True:
        return counts[1]
    return None

def count_eval2(exp):
    if exp == '0':
        return (1, 0)
    if exp == '1':
        return (0, 1)
    
    currcount = (0, 0)
    for i in range(len(exp)):
        if exp[i] in ['&', '|', '^']:
            countleft = count_eval2(exp[:i])
            countright = count_eval2(exp[i+1:])
            counts = calc_counts(countleft, countright, exp[i])
            currcount = add_tuple(currcount, counts)

    return currcount


def add_tuple(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

def calc_counts(left, right, exp):
    truetrue = left[1] * right[1]
    truefalse = left[1] * right[0]
    falsetrue = left[0] * right[1]
    falsefalse = left[0] * right[0]

    if exp == '&':
        return (truefalse + falsetrue + falsefalse, truetrue)
    if exp == '|':
        return (falsefalse, truetrue + truefalse + falsetrue)
    if exp == '^':
        return (truetrue + falsefalse, truefalse + falsetrue)
    return None

print(count_eval('1^0|0|1', False))
print(count_eval('0&0&0&1^1|0', True))
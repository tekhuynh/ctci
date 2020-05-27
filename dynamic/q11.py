def ways(n):
    return ways2(n, (25, 10, 5, 1), 0, dict())

def ways2(n, denoms, index, memo):
    if n == 0:
        return 1
    if index == len(denoms) - 1:
        if n % denoms[index] == 0:
            return 1
        return 0

    if has_memo(n, index, memo):
        return memo[n][index]

    num_ways = 0
    nn = n
    while nn >= 0:
        num_ways += ways2(nn, denoms, index + 1, memo)
        nn -= denoms[index]
    
    add_memo(n, index, memo, num_ways)
    return num_ways

def add_memo(n, index, memo, ways):
    if not n in memo:
        memo[n] = dict()
    memo[n][index] = ways

def has_memo(n, index, memo):
    if not n in memo:
        return False
    if not index in memo[n]:
        return False
    return True

i = int(input())
print(ways(i))
def countways(n):
    memo = [0] * (n+1)
    return countwaysh(n, memo)

def countwaysh(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    if memo[n]:
        return memo[n]
    
    memo[n] = countwaysh(n-1, memo) + countwaysh(n-2, memo) + countwaysh(n-3, memo)
    return memo[n]

print(countways(int(input())))
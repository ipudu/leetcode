# recursion O(3^n)

def triple_step(n):
    if n  == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)


# dynamic programming O(n)

def _triple_step(n):

    ans = [1, 2, 4]

    if n <= 3:
        return ans[n-1]
    
    for i in range(4, n+1):
        ans[i] = ans[i-1] + ans[i-2] + ans[i-3]
    
    return ans[-1]
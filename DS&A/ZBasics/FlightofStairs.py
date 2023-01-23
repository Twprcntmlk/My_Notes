def solve(self, n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1

    for idx in range(2,len(dp)):
        dp[idx] = (dp[idx - 1] + dp[idx - 2]) % (10 ** 9 + 7)
    return dp[-1]

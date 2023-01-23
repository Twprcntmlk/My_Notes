# Given two strings a and b, return the length of their longest common subsequence.


def solve(a, b):
    dp = [[0]*(len(a)+1) for _ in range(len(b)+1)]

    for i in range(1,len(b)+1): #b

        for j in range(1,len(a)+1): #a

            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

            if b[i-1] == a[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
    print(dp)
    return dp[-1][-1]

# for each string if b[i-1] == a[j-1]: carry 1 down to mark that it is sequence


a = "abcvcb"
b = "bvc"
print(solve(b, a))

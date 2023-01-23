# O(n) time O(1) space
def knightDialer(n):
        arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for x in range(n-1): #minus 1 because we already have first possible which is 1
            dp = [0 for _ in range(10)]
            dp[0] = arr[5] + arr[7] #from the 1
            dp[1] = arr[6] + arr[8]#from the 2
            dp[2] = arr[3] + arr[7]#from the 3
            dp[3] = arr[2] + arr[8] + arr[9]#from the 4
            dp[4] = 0 #from the 5
            dp[5] = arr[0] + arr[6] + arr[9]#from the 6
            dp[6] = arr[1] + arr[5]#from the 7
            dp[7] = arr[0] + arr[2]#from the 8
            dp[8] = arr[1] + arr[3]#from the 9
            dp[9] = arr[3] + arr[5]#from the 0
            arr = dp
        return sum(arr) % (10**9+7)

def knightDialer(n):
    prev_keys = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8],
    4: [3, 9, 0], 5: [], 6: [0,1,7], 7: [2,6], 8: [1,3],9: [2,4]}

    if n == 1:
        return 10

    dp = [0] * 10
    dp_prev = [1] * 10

    for i in range(2, n+1):
        for j in range(10):
            prevs = prev_keys[j]
            dp[j] = 0
            for key in prevs:
                dp[j] += dp_prev[key]
                dp[j] %= 1000000007
        dp_prev = dp.copy()

    return sum(dp) % 1000000007

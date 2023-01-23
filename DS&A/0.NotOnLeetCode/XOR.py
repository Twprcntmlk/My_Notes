
def minChanges(nums,k):
    freq = defaultdict(lambda: defaultdict(int))
    for i, x in enumerate(nums):
        freq[i%k][x] += 1 # freq by row

    n = 1 << 10
    dp = [0] + [-inf]*(n-1)
    for i in range(k):
        mx = max(dp)
        tmp = [0]*n
        for x, c in enumerate(dp):
            for xx, cc in freq[i].items():
                tmp[x^xx] = max(tmp[x^xx], c + cc, mx)
        dp = tmp
    return len(nums) - dp[0]

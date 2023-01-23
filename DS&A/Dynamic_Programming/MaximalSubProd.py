def solve(self, nums):
    ans = float("-inf")
    lo = hi = 1

    for x in nums:
        lo, hi = min(lo * x, hi * x, x), max(lo * x, hi * x, x)
        print(lo,hi)
        ans = max(ans, hi)
    return ans

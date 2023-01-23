#O(N) and O(N)
# Kadane’s Algorithm
def solve(self, nums, target):
    running_sum = defaultdict(int)
    running_sum[0] = 1

    ans, cur = 0, 0
    for n in nums: #current num
        cur += n #last number other than current ive seen
        ans += running_sum[cur - target] #if i
        running_sum[cur] += 1
    return ans

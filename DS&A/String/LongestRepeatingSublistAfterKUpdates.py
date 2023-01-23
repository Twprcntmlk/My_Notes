class Solution:
    def solve(self, nums, k):
        if not nums:
            return 0

        num_count = defaultdict(int)
        max_count = 0
        start = 0

        for end, num in enumerate(nums):
            num_count[num] += 1
            max_count = max(max_count, num_count[num])
            if end - start + 1 > max_count + k:
                num_count[nums[start]] -= 1
                start += 1

        return end - start + 1



class Solution:
    def solve(self, A, K):
        index = defaultdict(list)
        for i, x in enumerate(A):
            index[x].append(i)

        ans = 0
        for row in index.values():
            i = 0
            for j, y in enumerate(row):
                while row[j] - row[i] - (j - i) > K:
                    i += 1
                ans = max(ans, j - i + K + 1)

        return min(ans, len(A))

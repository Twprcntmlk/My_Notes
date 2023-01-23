# Iteration in the recurrence relation

The recurrence relation was dp(i) = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2]), because we are only allowed to climb 1 or 2 steps at a time. What if the question was rephrased so that we could take up to k steps at a time? The recurrence relation would become dynamic - it would be dp(i) = min(dp(j) + cost[j]) for all (i - k) <= j < i. We would need iteration in our recurrence relation.

# Kadane's Algorithm is an algorithm that can find the maximum sum subarray
1. best = negative infinity
2. current = 0
3. for num in nums:
    3.1. current = Max(current + num, num)
    3.2. best = Max(best, current)

4. return best

# Finding Indexs in Binaray Tree (When arrayed)
Parent- (index-1)/2
Left- index*2+1
Right- index*2+2

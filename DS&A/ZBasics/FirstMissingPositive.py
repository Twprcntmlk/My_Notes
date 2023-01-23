
def solve(nums):
    nums = set(nums)
    first = 1
    while first in nums:
        first += 1
    return first

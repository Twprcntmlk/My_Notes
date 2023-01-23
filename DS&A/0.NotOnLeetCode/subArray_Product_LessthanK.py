# Time Complexity: O(N), where N is the length of nums.
# Space Complexity: O(1), the space used by prod, left, and ans.
# Kadane’s Algorithm
def subArray(nums, k):
    if k <= 1:
        return 0
    productTillNow = 1
    result = 0
    leftPointer = 0
    for rightPointer, val in enumerate(nums):
        productTillNow *= val
        while productTillNow >= k:
            productTillNow /= nums[leftPointer]
            leftPointer += 1
        result += rightPointer - leftPointer + 1
    return result

print(subArray([10,5,2,6], 100))

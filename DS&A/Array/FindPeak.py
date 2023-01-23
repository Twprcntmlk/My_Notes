
def findPeakElement(nums):
    left , right = 0, len(nums) -1
    while left < right:
        # if there are only two elements mid is always the lower bound
        # so it makes sure [mid+1] is valid index
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

[1,2,1,3,5,6,4 ]

[1,7,1,3,5,6,4]

# Question 1:
# Given an Array A, find the minimum amplitude you can get after changing up to 3 elements.
# Amplitude is the range of the array (basically difference between largest and smallest element).

# Example 1:

# Input: [-1, 3, -1, 8, 5 4]
# Output: 2
# Explanation: we can change -1, -1, 8 to 3, 4 or 5
# Example 2:

# Input: [10, 10, 3, 4, 10]
# Output: 0
# Explanation: change 3 and 4 to 10
import math
def minAmplitude(sample):

    mean = sum(sample)/len(sample)

    # print(sample, mean, dp)
    MinValue = abs(min(sample) - mean)
    MaxValue = abs(max(sample) - mean)
    toChangeToValue = 0
    startFrom = None
    sample.sort()

    # print(MinValue, MaxValue)
    if MinValue > MaxValue:
        toChangeToValue = max(sample)
        startFrom = "front"
    else:
        toChangeToValue = min(sample)
        startFrom = "end"

    # print(sample,toChangeToValue,startFrom)

    if startFrom == "front":
        for x in range(0,3):
            sample[x] = toChangeToValue

    if startFrom == "end":
        for x in range(len(sample)-1,len(sample)-4,-1):
            sample[x] = toChangeToValue

    return(max(sample)-min(sample))




#[-1, -1, -1, -1, -1, 40], [-1, 40, 40, 40, 40, 40],[-1, -1, -1, -1, 40, 40], [-1, -1, 40, 40, 40, 40],
#
for sample in [[-5, -5, 0, 5, 5],[2, 3, 4, 5,-1, 1],[-1, -1, -1, -1, -1, 40],[-1, -1, -1, -1, -1, 40],[-1, -1, -1, -1, 40, 40], [-1, -1, 40, 40, 40, 40]]:
    print(minAmplitude(sample))
#[,
######################################################################################################################
def minDifference(nums):
    n = len(nums)
    if n <= 4:
        return 0
    min4 = nums[:4]
    max4 = nums[:4]
    for num in nums[4:]:
        idx, num_other = max([(i, val) for i, val in enumerate(min4)], key=lambda x: x[1])
        if num_other > num:
            min4[idx] = num
        idx, num_other = min([(i, val) for i, val in enumerate(max4)], key=lambda x: x[1])
        if num_other < num:
            max4[idx] = num
    nums8 = sorted(min4) + sorted(max4)
    minDiff = sys.maxsize
    for i in range(4):
        minDiff = min(minDiff, abs(nums8[i] - nums8[8 - 3 - 1 + i]))
    return minDiff

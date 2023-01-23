# Given an array of non-negative integers arr, your task is to find the number of ways it can be split into three non-empty contiguous subarrays such that the sum of the elements in the first subarray is less than or equal to the sum of the elements in the second subarray, and the sum of the elements in the second subarray is less than or equal to the sum of the elements in the third subarray.

# Note:

# Each element of arr must appear in exactly one of the three contiguous subarrays.
# Although the given numbers are 32-bit integers, the sum of the elements may exceed the limits of the 32-bit integer type.
# Example

# For arr = [1, 1, 1], the output should be countSubsegments(arr) = 1.

# The only way to split this array into three non-empty contiguous subarrays is [1], [1], [1]. This triple of subarrays satisfies the conditions (1 ≤ 1 ≤ 1), so the answer is 1.

# For arr = [1, 2, 0], the output should be countSubsegments(arr) = 0.

# The only way to split this array into three non-empty contiguous subarrays is [1], [2], [0]. This triple of subarrays doesn't satisfy the conditions (1 ≤ 2 > 0), so the answer is 0.

# For arr = [1, 2, 2, 2, 5, 0], the output should be countSubsegments(arr) = 3.

# If the first subarray is [1], there are 2 possibilities of choosing the second and the third one:
# Choose [2] as the second subarray and [2, 2, 5, 0] as the third subarray (1 ≤ 2 ≤ 9).
# Choose [2, 2] as the second subarray and [2, 5, 0] as the third subarray (1 ≤ 4 ≤ 7).
# If we choose a bigger second subarray, the sum of its elements will be at least 2 + 2 + 2 = 6, which is greater than the sum of the elements in any possible third subarray in that case.
# If the first subarray is [1, 2] there is only one way of choosing the other two subarrays:
# Choose [2, 2] as the second subarray and [5, 0] as the third subarray (3 ≤ 4 ≤ 5),
# If we choose a bigger or smaller subarray as the second one, the conditions won't be satisfied.
# There are 2 + 1 = 3 ways of dividing arr into three subarrays that meet the conditions, so the answer is 3

def countSubsegments(arr):
    pointerStartIdx = 0
    pointerEndIdx = len(arr)

    counterStart=0
    counterEnd=0
    while (pointerStartIdx+counterStart) < (pointerEndIdx-counterEnd):
        startTotal=0
        endTotal=0
        midTotal=0
        for x in range(0,pointerStartIdx+counterStart+1):
            startTotal+=arr[x]
        for y in reversed(range(len(arr)-counterEnd-1,len(arr))): #,len(arr)-1)
            endTotal+=arr[y]
        for z in range(pointerStartIdx+counterStart+1,pointerEndIdx-counterEnd-1):
            midTotal+=arr[z]

        
        counterStart+=1
        counterEnd+=1
        print(startTotal,midTotal, endTotal)#,

countSubsegments([1, 2, 2, 2, 5, 0])

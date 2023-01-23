# def pivotIndex( nums):
#     sumL = 0
#     sumR = sum(nums)
#     for i in range(len(nums)):
#         sumR -= nums[i]
#         if sumL == sumR:
#             return i
#         sumL += nums[i]
#     return -1

def pivotIndex(nums):
    leftIdx = 0
    rightIdx = len(nums)-1
    sumL = nums[0]
    for x in range(len(nums)):
       
        print(nums[:leftIdx+x])
        print(nums[leftIdx+1+x:])

print(pivotIndex([1,2,3]))

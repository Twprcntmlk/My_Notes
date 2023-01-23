def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    result=set()
    for idx, num in enumerate(nums):
        startIdx=1+idx
        endIdx=len(nums)-1
        while startIdx< endIdx:
            currentSum = num+nums[startIdx]+nums[endIdx]
            if currentSum==0:
                result.add((num, nums[startIdx], nums[endIdx]))
                startIdx+=1
                endIdx-=1
            elif currentSum > 0:
                endIdx-=1
            elif currentSum < 0:
                startIdx+= 1
    return result

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def TwoSum(nums,target):
    seen={}
    for x in nums:
        compliment = target-x
        if compliment in seen:
            return [compliment,seen[compliment]]
        else:
            seen[x]=compliment
    return -1

nums = [2,7,11,15]
target = 9
print(TwoSum(nums,target))

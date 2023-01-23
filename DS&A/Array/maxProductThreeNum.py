def solve(nums):
    nums.sort(reverse=True)
    print(nums)
    pos=nums[0]*nums[1]*nums[2]
    neg=nums[-1]*nums[-2]*nums[0]
    return(max(pos, neg))

nums = [-3, 1, 1, 0, 1]
print(solve(nums))

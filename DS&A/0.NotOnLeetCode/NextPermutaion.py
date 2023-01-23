def swap(num,idx1,idx2):
    num[idx1],num[idx2] = num[idx2], num[idx1]

def reverse(nums,idx1,idx2):
    while idx1 < idx2:
        swap(nums,idx1,idx2)
        idx1+=1
        idx2-=1

def nextPermutation(nums):
    #base cases
    if len(nums)==1:
        return
    if len(nums)==2:
        return swap(nums,0,1)

    start = len(nums)-2
    while start >=0 and nums[start] >= nums[start+1]:
        start-=1

    reverse(nums, start+1,len(nums)-1)
    if start == -1:
        return nums

    next_num = start+1

    while next_num < len(nums) and nums[next_num] <= nums[start]:
        next_num+=1
    swap(nums, next_num,start)
    return nums

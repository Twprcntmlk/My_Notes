# Time complexity : O(N) where N is the size of nums.
# Space complexity : O(N)
def rob(nums):
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        # In order to maximize your robbing,
        # you want to choose the case that will
        # result in the most amount of money.
    return dp[-1]

#issue case => [2,1,1,2]





# Time complexity : O(N) where N is the size of nums.
# Space complexity : O(1)

def Rob(nums) :
    #if just one house
    if len(nums)==1:
        return nums[0]
    hold=nums[0]
    n=len(nums)
    for i in range(2,n):
        nums[i]+=hold # one and three
        hold=max(hold,nums[i-1]) #compare 1,3 and 2

    return(max(nums[-1],nums[-2]))

def DeleteandEarn(nums):
    # if len(nums) == 1:
    #     return nums[0]
    # if len(nums) == 2:
    #     nums.sort()
    #     a = nums[0]
    #     b = nums[1]
    #     if a+1 == b:
    #         return b
    #     else:
    #         return a+b
    [1,2,4,99]
    m = max(nums)
    x = [0]*(m+1)
    for n in nums:
        x[n] += n

    dp = [0]*(m+1)
    #this takes care of the 1 case
    dp[1] = x[1]

    for i in range(2, m+1): #2,3,4
        dp[i] = max(dp[i-1], x[i]+dp[i-2]) #

        print("this is X",x,[i-2,i],(x[i]+dp[i-2]))
        print("this is DP",dp,[i-1],dp[i-1])


    return dp[m]

print(DeleteandEarn([1,1,1,1,2,2,2,2,3,3,3,3]))

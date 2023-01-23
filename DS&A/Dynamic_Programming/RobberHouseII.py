#Time complexity : O(N)
#Time space : O(N)
def rob(nums):
    # are going to go the robber problem twice and return the greater sum.
    n = len(nums)
    if n==1:
        return nums[0]
    if n==2:
        return max(nums[0], nums[1])
    ##################################################
    dp1 = [0]*(n-1)
    dp1[0] = nums[0]
    dp1[1] = max(nums[0], nums[1])
    for i in range(2,n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
    ####################################################
    dp2 = [0]*(n-1)
    dp2[0] = nums[1]
    dp2[1] = max(nums[1], nums[2])
    for i in range(2,n-1):
        dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i+1])

    return max(dp1[n-2],dp2[n-2])

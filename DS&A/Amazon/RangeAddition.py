
def getModifiedArray(length, updates):
        dp = [0] * (length+1)
        for update in updates:
            dp[update[0]]+= update[2]
            if update[1]+1 < len(dp)-1:
                dp[update[1]+1]+= -update[2]

        sum = 0
        for i,num in enumerate(dp):
            sum += num
            dp[i]= sum
        return dp[:-1]

# O(N)Time and Space
def change( amount, coins):
    dp = [0]*(amount+1)
    dp[0]=1     #[1,0,0,0,0,0]

    for coin in coins: #[1,2,5]
        for idx in range(1,len(dp)):
            if coin <= idx:
                dp[idx]+=dp[idx-coin]
    return dp[-1]
###################################################
#Can you make exact change/MONSOON UMBRELLA
# def change2( amount, coins):
#     dp = [0]*(amount+1)
#     dp[0]=1  #[1,0,0,0,0,0]
#     for coin in coins: #[1,2,5]
#         for idx in range(1,len(dp)):
#             if coin <= idx:
#                 dp[idx]+=dp[idx-coin]
#     if dp[-1] == 0:
#         return -1
#     else:
#         return dp[-1]

# amount=5
# coins=[3,5]
# print(change2(amount, coins))

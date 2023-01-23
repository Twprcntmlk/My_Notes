# Time Complexity: O(n) since we go through the list once
# Space Complexity:O(n) as our DP array is n size and that's how size works.

def solve(self, message):
    if not message:
        return 0
    dp = [0 for x in range(len(message) + 1)]

    dp[0] = 1
    dp[1] = 0 if message[0] == "0" else 1

    for i in range(2, len(message) + 1):
        if 0 < int(message[i - 1 : i]) <= 9:
            dp[i] += dp[i - 1]
        if 10 <= int(message[i - 2 : i]) <= 26:
            dp[i] += dp[i - 2]
    return dp[len(message)]

# Intuition
# s = "231"
# index 0: extra base offset. dp[0] = 1
# index 1: # of ways to parse "2" => dp[1] = 1
# index 2: # of ways to parse "23" => "2" and "23", dp[2] = 2
# index 3: # of ways to parse "231" => "2 3 1" and "23 1" => dp[3] = 2

# Implementation
# If the number is below 9, it can only possibly be 1 letter. If the number is above 9, it is 2 letters.

# In this case, we check twice.

# Example #1
# Let's go through our code for the input "123".

# Question 2:
# Given a string S, we can split S into 2 strings: S1 and S2. Return the number of ways S can be split such that the number of unique characters between S1 and S2 are the same.

# Example 1:
# Input: "aaaa"
# Output: 3
# Explanation: we can get a - aaa, aa - aa, aaa- a
# Example 2:

# Input: "bac"
# Output: 0
# Example 3:

# Input: "ababa"
# Output: 2
# Explanation: ab - aba, aba - ba

def splitString(string):
    result=[]
    for i in range(len(string)):
        front = string[:i+1]
        back = string[i+1:]
        if len(set(front)) == len(set(back)):
            result.append((front, back))
    return len(result)



for x in ["aaaa","bac","ababa"]:
    print(splitString(x))

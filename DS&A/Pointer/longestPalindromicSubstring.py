# Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

def longestPalindromicSubstring(string):

    ansStorage = {"longest":-1, 'string':""}

    def check(string, startIdx, endIdx):
        while startIdx >= 0 and endIdx < len(string) and string[startIdx] == string[endIdx]:
            startIdx-=1
            endIdx+=1
        return {"longest": endIdx-startIdx-1, 'string':string[startIdx+1:endIdx]}

    for Idx in range(len(string)):
        single = check(string, Idx, Idx)
        double = check(string, Idx, Idx+1)

        ansStorage["longest"]  = max(ansStorage["longest"], single["longest"], double["longest"])

        if ansStorage["longest"]  == single["longest"]:
            ansStorage["string"] = single["string"]
        if ansStorage["longest"]  == double["longest"] :
            ansStorage["string"] = double["string"]


    return {ansStorage["longest"],ansStorage["string"]}



for testString in ["a","aa","aba","asgegw","abbbbbbbbbbbb","abcdef"]:
    print(longestPalindromicSubstring(testString))

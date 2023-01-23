# Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# Example 1:
# Input: s = "aba"
# Output: true
# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:
# Input: s = "abc"
# Output: false
# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.

def subtractLetter(string, startIdx, endIdx):
    while startIdx < endIdx:
        if string[startIdx] != string[endIdx]:
            return False
    return True

def validPalindrome(string):
    startIdx =0
    endIdx = len(string)-1

    while startIdx < endIdx:
        if string[startIdx] != string[endIdx]:
            return subtractLetter(string, startIdx+1, endIdx) or subtractLetter(string, startIdx, endIdx-1)
        startIdx+=1
        endIdx-=1
    return True

for testString in ["aba","abca","abc"]:
    print(validPalindrome(testString))

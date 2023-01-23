# Time complexity: O(n), where n is a string length.
# Space complexity: O(n) for the stack.
def removeDuplicatesStack(s, k):
    stack = []
    for val in s:
        if not stack or stack[-1][0]!=val:
            stack.append([val,1]) #use the array to "backtrack delete"
        elif stack[-1][0]==val:
            stack[-1][1]+=1
        if stack[-1][1]>=k: #the backtracking
            stack.pop()
    return ''.join([stack[i][0]*stack[i][1] for i in range(len(stack))])
######################################################################################
def removeDuplicatesRecursive(s, k):
    result = []
    i = 0
    # this will find consecutive characters < than k and append and >k and ignore
    while i < len(s):
        hold = [s[i]]
        while 0 <= i < len(s)-1 and s[i] == s[i+1]:
            hold.append(s[i+1])
            i += 1
        i += 1
        if len(hold) >= k:
            continue
        else:
            result.append("".join(hold))
    result = "".join(result)

    #if nothing has changed result
    if len(result) == len(s):
        return result
    #recurse with new sting
    return removeDuplicatesRecursive(result,k)
###################################################################################
# BruteForce
# Time complexity: O(n^2 / k)
# Space complexity: O(1).
def removeDuplicates(s, k):
    length=-1
    while length !=len(s)-1:
        length=len(s)
        for idx in range(1,len(s)):
            if idx == 0 or s[idx]!=s[idx-1]:
                count=1
            elif idx > 0 and s[idx]==s[idx-1]:
                count+=1
            if count >= k:
                s=s[:idx-k+1]+s[idx+1:]
                break
    return s
#########################################################################################
# Solution 2: Two pointers
# Complexity: Time O(N), N is the length of s.
# Space: O(N).


# def removeDuplicates(self, s: str, k: int) -> str:
#     slow = 0
#     stack= []
#     s = [char for char in s] # for using enumerates

#     for fast, char in enumerate(s):
#         # if the char is new 1
#         s[slow] = char
#         if slow == 0 or s[slow - 1] != s[slow]:
#             stack.append(1)
#         #if the char is not new +1
#         else:
#             stack[-1] += 1
#             #if char >=k pop it off
#             if stack[-1] == k:
#                 #bring back my pointer for the amount i erased
#                 slow -= k
#                 stack.pop()
#         slow += 1
#     return "".join(s[:slow])
#####################################################################

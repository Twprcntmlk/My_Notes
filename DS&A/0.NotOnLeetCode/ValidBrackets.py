def bracket(string):
    dict = {'(' : ')', '[' : ']', '{' : '}'}
    if len(string) % 2 != 0:
        return False

    stack = []
    for char in string:
        if char in dict.keys():
            stack.append(char)
        else:
            if stack == []:
                return False
            lastchar = stack.pop()
            if char!= dict[lastchar]:
                return False
    return stack == []

string="((((()))))({)}[(])"
print(bracket(string))

# Follow Up:
# "<>", "aA", "\ /", "bB", ...,  How would you solve it ?


# def bracket(s):
#     hash={'(' :')','{' :'}','[' :']'}
#     stack=[]
#     for x in range(0, len(s)):

#         if len(stack)==0 and (s[x]=="}" or s[x]==")"or s[x]=="]"):
#             return False

#         if len(stack)==0 and (s[x]=="{" or s[x]=="("or s[x]=="["):
#             stack.append(s[x])

#         elif s[x] in hash:
#             if s[x]==stack[-1]:
#                  stack.append(s[x])
#             else:
#                 return False

#             if hash[stack[-1]] == s[x]:
#                 stack.pop()
#             else:
#                 return False

#     return len(stack)==0


# # s="[{]}"
# # s="[[ [[ [[ ]] ]] ]{ {{}}}"
# # s="}"
# # s="{"
# # s="("
# # s="[{]}"
# s="((((()))))({)}[(])"


# print(bracket(s))

# from itertools import combinations,permutations

# # list1_permutations = itertools.permutations(list1, len(list2))
# def getShortestUniqueSubstring(arr,str):
#     #table setup
#     table={}

#     permutation = list(permutations(arr, len(arr)))
#     for x in permutation:
#         permu = "".join(x)
#         table[permu]=0

#     print (table)

#     for x in range(len(str)-2):
#         if str[x:x+3] in table:
#             return str[x:x+3]
#     return False

# arr=['x','y','z']
# str="xyyzyzyx"

# print(getShortestUniqueSubstring(arr,str))
def getShortestUniqueSubstring(arr,str):
    currentMatch=str
    for idx in range(len(str)):
        for idy in range(idx+1,len(str)+1):
   
            if set(str[idx:idy]) == set(arr):
                if len(currentMatch) > len(str[idx:idy]):
                    currentMatch = str[idx:idy]
    return currentMatch

arr=['x','y','z']
str="xyyzyzyx"

print(getShortestUniqueSubstring(arr,str))

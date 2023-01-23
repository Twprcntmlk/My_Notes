# def howSum(num,arr):
#     # base case
#     if num == 0:
#         return 1
#     if num < 0:
#         return 0
#     result=0
#     for x in arr:
#         newNum = num - x
#         result+=howSum(newNum,arr)
#     return result



# # num =4
# # arr =[1,2]
# num =7
# arr =[5,3,4,7]
# print(howSum(num,arr))

def howSum(targetSum,numbers):
    # base case
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult  = howSum(remainder, numbers)
        #if we get to a targetSum > or = 0
        if  remainderResult !=None:
            result = remainderResult.append(num)
            return result
    return None



num =3

arr =[1,2]
# num =4
# arr =[1,2]
# num =7
# arr =[5,3,4,7]
print(howSum(num,arr))

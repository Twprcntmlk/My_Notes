# Time Complexity: O(N)
# Space Complexity O(N)

def Intervals(array, interval):
    # array.sort(), ask if needed
    # interval.sort(), ask if needed
    arrayIdx = 0
    intervalIdx = 1
    output = []
    hold=[]
    while arrayIdx < len(array) and intervalIdx < len(interval):

        if interval[intervalIdx-1] < array[arrayIdx] < interval[intervalIdx]:
            hold.append(array[arrayIdx])
            arrayIdx+=1

        elif array[arrayIdx] > interval[intervalIdx]:
            output.append(hold)
            hold=[]
            intervalIdx+=1
        else:
            arrayIdx+=1
    # take care of my endcase
    if hold:
        output.append(hold)
    return output

# array = [3,5,6,7,9,11,14,20,32]

# interval= [4,9,15]

# print(Intervals(array, interval))

# def Intervals(array, interval):
#     table={}
#     for x in array:
#         if x not in table:
#             table[x]=1
#         else:
#             table[x]+=1


#     for idx in range(1,len(intervals)):

#         intervals[idx-1]
#         intervals[idx]

# nums =[1,2,3,4,5,6,7,8,9]
# letters ="fsdifgbhifgbsdhilbfilebfilevbfliwbfluiwebfweilbfuilw"
# from collections import Counter
# print(Counter(letters).most_common()[::-1])

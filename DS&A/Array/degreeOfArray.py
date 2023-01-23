def findShortestSubArray(nums):
    minseen={}
    maxseen={}
    result =[]
    for i, j in enumerate(nums):
        if j not in minseen:
            minseen[j]=i
        else:
            maxseen[j]=i
    print(minseen)
    print(maxseen)
    for x in minseen:
        if x in maxseen:
            result.append(maxseen[x] -minseen[x] + 1)
    return min(result)


nums = [1,2,2,3,1]
print(findShortestSubArray(nums))

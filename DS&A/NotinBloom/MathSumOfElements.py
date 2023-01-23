def Max_Sum(arr, k):
    # To store the break point
    p = len(arr)
    # Sort the given array
    arr.sort()
    # Find the break point
    for i in range(0, len(arr)):
        # No need to look beyond i'th index
        if (arr[i] >= k):
            p = i
            break

    #do the traditional twoSum
    maxsum = 0
    a = 0
    b = 0
    # Find the required pair
    for i in range(0, p):
        for j in range(i + 1, p):
            if(arr[i] + arr[j] < k): #and arr[i] + arr[j] > maxsum
                maxsum = max(maxsum, arr[i] + arr[j])
                a = arr[i]
                b = arr[j]
    return(a, b)

Array = [5, 20, 110, 100, 64,];
k = 85;
print(Max_Sum(Array, k))

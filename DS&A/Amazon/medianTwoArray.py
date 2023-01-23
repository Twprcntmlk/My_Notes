#Time O(N) #Space O(N)
def findMedianSortedArrays(nums1, nums2):
    newsortedArray=[]

    i=j=0
    # sort arrays into new array
    while len(nums1)>i and len(nums2)>j:
        if nums1[i] < nums2[j]:
            newsortedArray.append(nums1[i])
            i+=1
        else:
            newsortedArray.append(nums2[j])
            j+=1
    while i < len(nums1):
        newsortedArray.append(nums1[i])
        i+=1
    while j < len(nums2):
        newsortedArray.append(nums2[j])
        j+=1

    # get median
    length=len(newsortedArray)

    if len(newsortedArray)%2!=0:
        return newsortedArray[(length//2)]
    else:
        return (newsortedArray[(length//2)-1]+newsortedArray[length//2])/2

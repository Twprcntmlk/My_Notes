def nextGreaterElement(nums1,nums2):
    table={}
    result=[-1]*len(nums1)
    for idx,num1 in enumerate(nums2):
        table[num1]=idx


    for idx,num2 in enumerate(nums1):
        start = table[num2]

        for i in range(start,len(nums2)):

            if nums2[start] < nums2[i]  :
                result[idx]=(nums2[i])
                break
    return result


##Stack solution
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    diff = {}
    #So I know nums1 and nums2 are SUBSETS and so I
    #I will talk through nums2 the larger and find the first largest and add to my dict.
    for idx, num in enumerate(nums2):
        while stack and stack[-1] < num:
            diff[stack.pop()] = num
        stack.append(num)

    # if it exist in my dict then put largest else -1
    for idx in range(len(nums1)):
        if nums1[idx] in diff:
            nums1[idx] = diff[nums1[idx]]
        else:
            nums1[idx] = -1

    return nums1

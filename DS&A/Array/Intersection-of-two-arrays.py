# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.



def intersection(nums1, nums2):

    set1 = set(nums1)
    set2 = set(nums2)
    return list(set2 & set1)


nums1 = [4,9,5]
nums2 = [4,4,8,9,9,5]
print(intersection(nums1, nums2))

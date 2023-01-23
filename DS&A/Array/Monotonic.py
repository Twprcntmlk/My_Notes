def isMonotonic(array):
	isNonDecreasing = True
	isNonIncreasing = True

	for i in range(1,len(array)):
		if array[i] < array[i-1]:
			isNonDecreasing = False
		if array[i] > array[i-1]:
			isNonIncreasing = False

	return isNonDecreasing or isNonIncreasing

nums = [1,2,2,3]
nums1 = [6,5,4,4]
nums2 = [1,3,2]
nums3 = [1,2,4,5]
nums4 = [1,1,1]

print(isMonotonic(nums))

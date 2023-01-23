def binarySearch(array, target):
    # Write your code here.
	return binarySearchHelper(array, target, 0, len(array)-1)

    def binarySearchHelper (array, target, left, right):
        if left > right:
            return -1
        middle = (left + right) // 2
        match =  array[middle]
        if target == match:
            return middle
        elif target < match:
            return binarySearchHelper(array, target, left, middle-1)
        else:
            return binarySearchHelper(array, target, middle+1,right )

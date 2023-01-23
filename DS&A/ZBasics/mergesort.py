def mergeSortedArrays (leftArray, rightArray):
	sortedArray = [None] * (len(leftArray) + len(rightArray)) #[None, None, None, None, ...]
	k=0 #sortedArray
	i=0 #leftArray
	j=0 #rightArray
	#while there are still number in BOTH lists compare the first numbers in list
	while i < len(leftArray) and j < len(rightArray):
		if leftArray[i] <= rightArray[j]:
			sortedArray[k] = leftArray[i]
			i+=1
		else:
			sortedArray[k] = rightArray[j]
			j+=1
		k+=1
	#While there are only values on left Array (should already be sorted) [4,5,6][] ==> [1,2,3]
	while i < len(leftArray):
		sortedArray[k]=leftArray[i]
		i+=1
		k+=1
	#While there are only values on right Array (should already be sorted) [][4,5,6] ==>[1,2,3]
	while j < len(rightArray):
		sortedArray[k]=rightArray[j]
		j+=1
		k+=1
	return sortedArray

def mergeSort(array):
	#base case of nothing to sort
	if len(array) == 1:
		return array
	# find middle index and split
	midIdx =  len(array)//2 #ex. 2.5 ==> 2
	leftArray=array[:midIdx]
	rightArray=array[midIdx:]
	# this should recurvsive get to either [ 2, 3 ] or  [1]
	return mergeSortedArrays(mergeSort(leftArray), mergeSort(rightArray))

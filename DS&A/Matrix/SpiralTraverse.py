def IterativespiralTraverse(array):
    if matrix == []:
        return []
    ans=[]
    startRow, endRow = 0, len(matrix)-1
    startCol, endCol = 0, len(matrix[0])-1
    while (startRow <= endRow) and  (startCol <= endCol):

        for col in range(startCol, endCol+1):
            ans.append(matrix[startRow][col])

        for row in range(startRow+1, endRow+1):
            ans.append(matrix[row][endCol])

        for col in reversed(range (startCol, endCol)):
            if startRow == endRow:
                break
            ans.append(matrix[endRow][col])

        for row in reversed(range(startRow+1, endRow)):
            if startCol == endCol:
                break
            ans.append(matrix[row][startCol])

        startRow +=1
        endRow -=1
        startCol  +=1
        endCol -=1
    return ans

# def RecursivespiralTraverse(array):
# 	ans = []
# 	spiralfill(array, ans, 0,len(array)-1,0, len(array[0])-1)
# 	return ans

# def spiralfill(array, ans,startRow,endRow,startCol, endCol):
# 	if (startRow > endRow) or (startCol > endCol):
# 		return ans
# 	for col in range(startCol, endCol+1):
# 		ans.append(array[startRow][col])

# 	for row in range(startRow+1, endRow+1):
# 		ans.append(array[row][endCol])

# 	for col in reversed(range(startCol, endCol)):
# 		if startRow == endRow:
# 			break
# 		ans.append(array[endRow][col])

# 	for row in reversed(range(startRow+1, endRow)):
# 		if startCol == endCol:
# 			break
# 		ans.append(array[row][startCol])
# 	startRow+=1
# 	endRow-=1
# 	startCol+=1
# 	endCol-=1
# 	spiralfill(array,ans,startRow,endRow,startCol, endCol )

# print(IterativespiralTraverse())
# print(RecursivespiralTraverse())

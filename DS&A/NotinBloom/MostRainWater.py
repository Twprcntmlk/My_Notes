def maxArea(height):
	#variables
	startIdx=0
	endIdx=len(height)-1
	currentMax=0
	currentmin=0

	while startIdx < endIdx:
		if height[startIdx] > currentmin:
			currentArea = min( height[startIdx], height[endIdx])*(endIdx-startIdx)
			currentmin=min(height [startIdx], height[endIdx])
			currentMax = max(currentMax,currentArea)
			startIdx+=1
		elif height[endIdx] > currentmin:
			currentArea = min( height[startIdx], height[endIdx])*(endIdx-startIdx)
			currentmin=min(height [startIdx], height[endIdx])
			currentMax = max(currentMax,currentArea)
			endIdx-=1
		else:
			startIdx+=1
			endIdx-=1
	return currentMax

heights =[[1,8,6,2,5,4,8,3,7],[1,1],[4,3,2,1,4],[1,2,1]]
for height in heights:
	print(maxArea(height))



#######################################################################
def maxArea(height):
	#variables
	startIdx=0
	endIdx=len(height)-1
	currentMax=0

## iterate from the left height = [1,8,6,2,5,4,8,3,7]

	for idx, x in enumerate(height):
		currentArea = min(x, height[len(height)-1])*((len(height)-2)-idx)
		currentMax = max(currentMax,currentArea )

##iterate from the right
	reversedList=list(reversed(height))
	for idx, x in enumerate(reversedList):
	# For idx in range(len(height)-1,-1,-1):
		currentArea = min(x, height[len(height)-1])*((len(height)-2)-idx)
		currentMax = max(currentMax,currentArea )

##iterate from both sides
	while startIdx < endIdx:
		currentArea = min( height [startIdx] , height[endIdx])*(endIdx-startIdx)
		currentMax = max(currentMax,currentArea)
		startIdx+=1
		endIdx-=1

	return currentMax

heights =[[1,8,6,2,5,4,8,3,7],[1,1],[4,3,2,1,4],[1,2,1]]
for height in heights:
	print(maxArea(height))

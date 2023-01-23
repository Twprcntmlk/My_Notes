# Problem: Minimum Domino Rotations For Equal Row
# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

# If it cannot be done, return -1.

# Input:
# tops = [2,1,2,4,2,2],
# bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation:
# The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
# Example 2:

# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation:
# In this case, it is not possible to rotate the dominoes to make one row of values equal.

def DominoRotations(tops,bottoms):
    from collections import Counter;
    dominoPairs = list(zip(tops, bottoms))
    dpTop = [-1]*len(tops)
    dpBottom = [-1]*len(bottoms)
    # if dominoPairs[0][0] == dominoPairs[0][1]:
    dpTop[0]=-1
    dpBottom[0]=-1


    table = Counter(tops+bottoms)
    NumsToConsider = []
    for k,v in table.items():
        if v >= len(dominoPairs):
            NumsToConsider.append(k)

    if len(NumsToConsider) == 0:
        return -1


    for num in NumsToConsider: ## it's always at most 2
        for i in range(len(dominoPairs)):
            if dominoPairs[i][0] == dominoPairs[i][1]:
                dpTop[i] = 0
                dpBottom[i] = 0
            elif num == dominoPairs[i][0] and dpTop[i] != 1:
                dpTop[i] = 1
            elif num == dominoPairs[i][1] and dpBottom[i] != 1:
                dpBottom[i] = 1

    # count = 0
    print(dpTop)
    print(dpBottom)
    for i in range(0,len(dominoPairs)):
        if dpTop[i] == -1 and dpBottom[i] == -1:
            return -1


    dp = list(zip(dpTop, dpBottom))
    print(dp)
    return min(dp.count((1,-1)), dp.count((-1,1)))



tops =    [2,1,2,4,2,2]
bottoms = [5,2,6,2,5,2]
# tops =    [2,2,2,2,2,2]
# bottoms = [5,5,5,5,5,5]
# tops =    [3,5,1,2,3]
# bottoms = [3,6,3,3,4]
print(DominoRotations(tops,bottoms))

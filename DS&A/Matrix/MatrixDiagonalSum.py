def diagonalSum(mat):
    count=0
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if row == col :
                count+=mat[row][col]
            #cool part [0,4] [1,3] NOT[2,2] [3,1] [4,0]
            if (len(mat)-1==row+col) and (row!=col):
                count+=mat[row][col]
    return count

def solve(self, matrix):

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            fromLeft=matrix[row][col]
            fromAbove=matrix[row][col]
            if  0 < row < len(matrix) :
                fromLeft = matrix[row][col] + matrix[row-1][col]
            if  0 < col < len(matrix[0]):
                fromAbove = matrix[row][col]+matrix[row][col - 1]
            matrix[row][col] = max(fromLeft, fromAbove)
    return matrix[-1][-1]

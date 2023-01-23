class Solution:
    def solve(self, matrix):

        for col in range(len(matrix[0])):
            for row in range(col,len(matrix)):
                print(matrix[col][row])
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

        return matrix

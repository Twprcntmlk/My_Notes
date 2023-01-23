# Time Complexity = O(N*M)
# Space Complexity = O(1)
def solve(self, matrix):
    sides=0
    ###################################
    def helper(row,col):
        count=0
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x = row +dx
            y = col + dy
            if (x<0 or y<0 or x>=len(matrix) or y>=len(matrix[0])) or matrix[x][y]==0:
                count+=1
        return count
    ####################################
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][col]==1:
                sides+=helper(row,col)
    return sides

#Number of Islands  #################################################################
def numIslandsdfs(grid):
    count = 0

    def dfs(grid, x, y):
        grid[x][y] = "0"
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for dx, dy in directions:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x+dx][y+dy] == "1":
                dfs(grid, x + dx, y + dy)
        return

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                count += 1
                dfs(grid, row, col)
    return count
############################################################
def numIslandsbfs(grid):
    visited=set()
    count = 0

    def bfs(grid, x, y, visited):
        queue = [(x, y)]

        while queue:
            sx, sy = queue.pop(0)
            visited.add((sx, sy))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dx, dy in directions:
                x = sx + dx
                y = sy + dy
                if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and (x, y) not in visited and grid[x][y] == "1":
                    visited.add((x, y))
                    queue.append((x, y))


    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1" and (row,col) not in visited:
                count += 1
                bfs(grid, row, col, visited)
    return count

###BomberMan
def solve(matrix):
    count=0
    rowList, colList = set(), set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                rowList.add(row)
                colList.add(col)
                
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i not in rowList and j not in colList:
                count+=1
    return count

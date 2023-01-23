def gameOfLife(grid):

    copy_board = [[grid[row][col] for col in range(len(grid[0]))] for row in range(len(grid))]
    def helper(tempgrid, x, y):
        count=0

        directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        for dx, dy in directions:
            if 0 <= x + dx < len(tempgrid) and 0 <= y + dy < len(tempgrid[0]) and tempgrid[x+dx][y+dy] == 1:
                count+=1
        return count

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid[row][col] = helper(copy_board, row, col)


    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if copy_board[row][col]== 1:
                if grid[row][col] < 2: #Any live cell with fewer than two live neighbors dies as if caused by under-population.
                    grid[row][col] = 0
                if grid[row][col] == 2 or grid[row][col] == 3:  #Any live cell with two or three live neighbors lives on to the next generation.
                    grid[row][col] = 1
                if grid[row][col] > 3:   #Any live cell with more than three live neighbors dies, as if by over-population.
                    grid[row][col] = 0

            if copy_board[row][col]==0:
                if grid[row][col] == 3:  #Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                    grid[row][col] = 1
                elif grid[row][col] != 3:
                    grid[row][col] = 0
    return grid
# grid = [
#   [1,1,0,0,0],
#   [1,1,0,0,0],
#   [0,0,1,0,0],
#   [0,0,0,1,1]
# ]
grid = [
  [1,1,0],
  [1,0,0],
  [0,0,0]
]
print(gameOfLife(grid))

# def numIslandsbfs(grid):
#     visited=set()
#     count = 0

#     def bfs(grid, x, y, visited):
#         queue = [(x, y)]

#         while queue:
#             sx, sy = queue.pop(0)
#             visited.add((sx, sy))
#             directions = [[1,0],[-1,0],[0,1],[0,-1]]
#             for dx, dy in directions:
#                 x = sx + dx
#                 y = sy + dy
#                 if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and (x, y) not in visited and grid[x][y] == "1":
#                     visited.add((x, y))
#                     queue.append((x, y))


#     for row in range(len(grid)):
#         for col in range(len(grid[0])):
#             if grid[row][col] == "1" and (row,col) not in visited:
#                 count += 1
#                 bfs(grid, row, col, visited)
#     return count


# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# print(numIslandsbfs(grid))

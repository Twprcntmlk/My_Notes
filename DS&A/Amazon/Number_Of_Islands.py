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


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslandsdfs(grid))

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


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslandsbfs(grid))

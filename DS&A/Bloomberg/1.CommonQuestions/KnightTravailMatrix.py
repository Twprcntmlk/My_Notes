#Time Complexity: O(N*3^L) (3^L == number of traversals and the length of the word)
#Space Complexity: O(n)

def exist(n, startCol,startRow, endCol, endRow):
    visited = set([(startRow, startCol)])
    queue = [(startRow, startCol, 0)]  # (x, y, step)
    directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

    while queue:
        row, col, step = queue.pop(0)
        if row == endRow and  col == endCol:
            return step

        for dx, dy in directions:
            new_x, new_y = row + dx, col + dy

            if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, step+1))
##########################################################

for n, startCol,startRow, endCol, endRow in [[8,0,0,1,1]]:
    print(exist(n, startCol,startRow, endCol, endRow))

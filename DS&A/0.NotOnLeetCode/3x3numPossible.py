class Node:
    def __init__(self, val):
        self.val = val
        self.directions = []

def count_pos(start, hops):
    count = 0

    def dfs(node, hops):
        if not node:
            return
        if hops == 0:
            count += 1

        for direction in node.directions:
            dfs(direction, hops - 1)

    dfs(start, hops)
    return count

##########################################################################################
def count_unique_pos(start, hops):
    count = 0
    visited = set()

    def dfs(node, hops, path):
        if not node:
            return

        if hops == 0:
            if path not in visited:
                visited.add(path)
                count += 1

        for direction in node.directions:
            dfs(direction, hops - 1, path + str(direction.val))

    dfs(start, hops, "")
    return count

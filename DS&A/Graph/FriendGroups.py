# Time Complexity: O(N+M) where n=number of vertices and m is edges.
# Space Complexity: O(n). where n=number of vertices.

def solve(self, friends):
    #[[1], [0, 2], [1], [4], [3], []]
    n = len(friends)
    visited = [False] * len(friends) #Visited array to keep track of visited vertices.
    count = 0 #count=0 to count connected components which is basically groups of friends.

    for i in range(n):
        if visited[i] == False:
            count += 1
            dfs(visited, i, friends)
    return count


    def dfs(visited, i, friends):
        visited[i] = True
        for j in friends[i]:
            if visited[j] == False:
                dfs(visited, j, friends)
        return

# we will simply iterate from 0th vertice and set its connected vertices true so it's like one graph in which 0th vertice is present.
# In next iteration next unvisited vertice will be picked and so on.

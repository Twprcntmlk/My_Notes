from collections import defaultdict;
import math
def minimumTreePath(n, edges, visitNodes):
    graph = defaultdict(list)
    for edge in edges:
       graph[edge[0]].append(edge[1])
       graph[edge[1]].append(edge[0])
    print(graph)

    allPath=[]
    def dfs(node, path, seen):
        # print(path)
        check = all(item in path for item in visitNodes)
        if check and path[-1] == n:
            allPath.append(path)

        for child in graph[node]:
            if child in visitNodes:
                seen+=1
                dfs(child, path+[node], seen)
            if path.count(child)==3:
                break
            else:
                dfs(child, path+[node], seen)
    dfs(1,[],0)
    smallestDistance = math.inf

    for x in allPath:
       smallestDistance= min(smallestDistance, len(x))
    print(allPath)
    return smallestDistance




n=5
edges=[[1,2,],[1,3,4],[3,4,2],[3,5]]
visitNodes=[2,4]
print(minimumTreePath(n, edges, visitNodes))

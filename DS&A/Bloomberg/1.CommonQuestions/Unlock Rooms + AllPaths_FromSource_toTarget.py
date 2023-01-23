# Space Complexity:O(N*2^N)
# Time Complexity: O(N*2^N)
def allPathsSourceTarget(graph):
    def dfs(node,path):
        if node == len(graph)-1: # if my node reachs my target, because this is acyclic
            output.append(path)
        for nextNodeRef in graph[node]:
            dfs(nextNodeRef,path+[nextNodeRef])
    output=[]
    dfs(0,[0])
    return output
#########################################################################################
def allPathsSourceTargetStack(graph):
    result = []
    target = len(graph) - 1
    stack = [([0], graph[0])]

    while stack:
        for _ in range(len(stack)):
            path, nodes = stack.pop()

            if path and path[-1] == target:
                result.append(path)

            for neighbor in nodes:
                stack.append((path + [neighbor], graph[neighbor]))
    return result
##############################################################################
def allPathsSourceTargetWITHCYCLE(graph):
    seen=set()
    def dfs(node,path):
        seen.add(node)

        if node == len(graph)-1:
            output.append(path)
        for nextNodeRef in graph[node]:
            if nextNodeRef not in seen:
              dfs(nextNodeRef,path+[nextNodeRef])
            else:
              continue
    output=[]
    dfs(0,[0])
    return output
### UnlockRooms #################################################
def solve(rooms):
    seen=set()

    def dfs(node, connections):
        seen.add(node)

        for nextRoom in rooms[node]:

            if nextRoom not in seen:
                dfs(nextRoom, connections+[nextRoom])
            else:
                continue
    dfs(0,[1,3])
    return len(seen)==len(rooms)

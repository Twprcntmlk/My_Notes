# Time Complexity: O(2^N-2) Space Complexity: O(2^N-2)
# num of Paths x num of Nodes and -2 because need to have at least 2 nodes
def allPathsSourceTarget(graph):
    #graph = [[1,2],[3],[3],[]]
    output = []
    def get_paths(node, graph, path, target):
        if node == target:
            output.append(path+[node])
        else:
            for item in graph[node]:
                get_paths(item, graph, path+[node], target)
    source, target = 0, len(graph)-1
    get_paths(source, graph, [], target)
    return output

# For N=2, 1 paths, 2^0
# For N=3, 2 paths, 2^1
# For N=4, 4 paths, 2^2
# For N=5, 2 paths, 2^3

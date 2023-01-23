from collections import defaultdict;

def findOrder(numCourses, prerequisites):
    in_degree = defaultdict(int)
    adjList = defaultdict(set)

    for pair in prerequisites:
        in_degree[pair[0]] += 1
        adjList[pair[1]].add(pair[0])

    ######
    # Kahn's algorithm
    top_sort = []
    queue = []

    for key, value in in_degree.items():
        if value == 0:
            queue.append(key)

    while len(queue) > 0:
        vertex = queue.pop(0)
        top_sort.append(vertex)

        for child in adjList[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    ######
    if len(top_sort) == numCourses:
        return top_sort
    else:
        return []

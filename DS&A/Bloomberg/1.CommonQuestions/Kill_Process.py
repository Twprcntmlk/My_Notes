# Time complexity : O(n). We need to traverse over the ppid array of size n once.
# Space complexity : O(n). size of the map
def killProcessBFS(pid, ppid, kill):
        graph = defaultdict(set)
        for i in range(len(pid)):
            graph[ppid[i]].add(pid[i])
        queue= [kill]
        result = []
        while queue:
            node = queue.pop()
            res.append(node)
            for children in graph[node]:
                queue.append(children)
        return result

# Time complexity : O(n). We need to traverse over the ppid array of size n once.
# Space complexity : O(n). size of the map
def killProcessDFS(pid, ppid, kill):
        graph = defaultdict(set)
        for i in range(len(pid)):
            graph[ppid[i]].add(pid[i])
        ans = []
        ######################################
        def dfs(node):
            ans.append(node)
            if not node:  # or not in graph
                return
            for c in graph[node]:
                dfs(c)
         #############################################
        dfs(kill)
        return ans

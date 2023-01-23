# Time Complexity: O(NlogN)
# Space Complexity: O(N)
def verticalOrder(root):
    nodeList = []
    queue = [(root, 0,0)]
    while queue:
        node, column, row = queue.pop(0)
        if node :
            nodeList.append((column,row,node.val))
            queue.append((node.left, column - 1, row+1))
            queue.append((node.right, column + 1,row+1))
    result=[]
    nodeList.sort()

    table=defaultdict(list)
    for col, row, val in nodeList:
        table[col].append(val)

    return table.values()

def verticalOrder(root):

    nodeList = []
    def dfs(node,col,row):
        if not node:
            return
        nodeList.append((col,row, node.val))
        dfs(node.right, col+1, row+1)
        dfs(node.left, col-1, row+1)

    dfs(root,0,0)

    nodeList.sort()

    table=defaultdict(list)
    for col, row, val in nodeList:
        table[col].append(val)

    return table.values()

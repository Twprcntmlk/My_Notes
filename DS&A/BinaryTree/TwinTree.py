def solve(self, root0, root1):
    def  dfs(node0, node1):
        if not node0 or not node1:
            return not node0 and not node1

        if node0.val != node1.val :
            return False

        return dfs( node0.right, node1.right) and  dfs( node0.left, node1.left)

    return dfs(root0, root1)

def solve(self, node0, node1):

    if not node0:
        return node1
    if not node1:
        return node0

    node0.left=self.solve(node0.left,node1.left)
    node0.val+=node1.val
    node0.right=self.solve(node0.right,node1.right)

    return node0

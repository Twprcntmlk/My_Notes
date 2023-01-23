# Time complexity: O(n + n) = O(2n) =
# Space complexity: O(n)

class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return None

        def dfs_copy(node):
            if not node:
                return

            copy[node] = NodeCopy(node.val)

            dfs_copy(node.left)
            dfs_copy(node.right)

            return node



        def dfs_connect(node):
            if not node:
                return

            if node.left:
                copy[node].left = copy[node.left]
            if node.right:
                copy[node].right = copy[node.right]
            if node.random:
                copy[node].random = copy[node.random]

            dfs_connect(node.left)
            dfs_connect(node.right)

            return node

        copy = {}
        dfs_copy(root)
        dfs_connect(root)
        return copy[root]



########################################################################################################
def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
    if not root:
        return None

    def dfs_copy(node):
        if not node:
            return

        copy[node] = NodeCopy(node.val)

        dfs_copy(node.left)
        dfs_copy(node.right)

        return node

    def dfs_connect(node):
        if not node:
            return

        if node.left:
            copy[node].left = copy[node.left]
        if node.right:
            copy[node].right = copy[node.right]
        if node.random:
            copy[node].random = copy[node.random]

        dfs_connect(node.left)
        dfs_connect(node.right)

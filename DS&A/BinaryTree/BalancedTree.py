def isBalanced(root):

     def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                self.ans = False
            return 1 + max(left, right)

        self.ans = True
        dfs(root)
        return self.ans




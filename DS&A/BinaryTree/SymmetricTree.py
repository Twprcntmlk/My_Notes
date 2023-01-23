    def solve(self, root):
        def helper(nodeLeft,nodeRight):
            if nodeLeft is None and nodeRight is None:
                return True
            elif nodeLeft is None or nodeRight is None:
                return False
            else:
               return nodeLeft.val == nodeRight.val and helper(nodeLeft.left,nodeRight.right) and helper(nodeLeft.right, nodeRight.left)
        if root == None:
            return True
        else:
            return helper(root.left,root.right)

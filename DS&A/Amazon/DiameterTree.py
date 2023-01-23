def diameterOfBinaryTreeDFS(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            if not node:
				# my parent is a leaf (and the leaf base case has diameter = 0)
                return 0
            # len(longest path from r.left/right to some leaf)
            left= dfs(node.left)
            right = dfs(node.right)
            # diameter including this node is # edges on left path + #E(right)
            length = left + right
            diameter = max(length, diameter)

            # tell my parent the length of the longest path to a leaf that goes through me
			# this is just the maximum of the same problem but for each of my children and +1
			#  to include the edge from me to the longest child
            return max(left, right) + 1

        dfs(root)
        return diameter

## FOLLOW UP WHAT IF I WANT NODE LIST ######################################################################
def diameterOfBinaryTree(root):
    if not root:
        return None

    max_length = 0
    node_list = []

    def dfs(node):
        if not node:
            return (0, [])

        left_max, left_node_list = dfs(node.left)
        right_max, right_node_list = dfs(node.right)

        if left_max + right_max > max_length:
            max_length = left_max + right_max
            node_list = left_node_list + right_node_list

        if left_max > right_max:
            return (left_max+1, left_node_list + [node])
        else:
            return (right_max+1, right_node_list + [node])

    dfs(root)
    return max_length

# Given a binary tree, with characters as nodes, return the path from leaf node to root, but smallest alphabetically
# for example, A is root, DEA, BAEA, BCA are all paths from leaf to the root A, but return BCA because B comes DEA and BCA is shorter than BAEA

def smallestFromLeaf(root):
        paths = []

        def dfs(node, string):
            # Translate node value to letter via ASCII
            string += chr(node.val + 97)

            if node.left:
                dfs(node.left, string)
            if node.right:
                dfs(node.right, string)
            # At leaf node, add reversed tree path to "paths"
            if not node.right and not node.left:
                paths.append(string)

        dfs(root, '')
        # Sort in lexicographical order and return first path
        paths.sort()
        return paths[0]

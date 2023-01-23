# Time complexity: O(n) Space complexity: O(n)
def isValidBSTRecursive(root):

    def validate(node, low=-math.inf, high=math.inf):
        # Empty trees are valid BSTs.
        if not node:
            return True
        # The current node's value must be between low and high.
        # i.e for right side lower will be -inf unless it has a left
        if node.val <= low or node.val >= high:
            return False

        # The left and right subtree must also be valid.
        return (validate(node.right, node.val, high) and
                validate(node.left, low, node.val))

    return validate(root)
##############################################################################################
def isValidBSTIterative(root):
    if not root:
        return True

    stack = [(root, -math.inf, math.inf)]
    while stack:
        node, lower, upper = stack.pop()
        if not node:
            continue
        val = node.val
        if val <= lower or val >= upper:
            return False
        stack.append((node.right, val, upper))
        stack.append((node.left, lower, val))
    return True

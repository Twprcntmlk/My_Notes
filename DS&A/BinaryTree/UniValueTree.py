# Univalue tree is a tree where all nodes under it have the same value.
def solve(self, root):
    count = [0]
    self.rec(root, count)
    return count[0]

def rec(self, root, count):
    if not root:
        return True

    left = self.rec(root.left, count)
    right = self.rec(root.right, count)

    if left == False or right == False:
        return False

    if root.left and root.val != root.left.val:
        return False

    if root.right and root.val != root.right.val:
        return False

    count[0] += 1
    return True

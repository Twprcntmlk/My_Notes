# Look at first node that is None
# For a complete binary tree the spaces after this node will also be None
# Else the tree is not complete

# Runtime Complexity: O(N) where N is the number of nodes in the tree
# Space Complexity: O(N) for putting the last level of a complete tree into the queue

from collections import deque

def isCompleteTree(root):
    deq = deque([root])

    while deq:
        curr = deq.popleft()
        if curr == None:
            return not any(deq)
        deq.append(curr.left)
        deq.append(curr.right)

    return True

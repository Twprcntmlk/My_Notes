# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def solve(self, node):
        hare = tortoise = node
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next

        right = None
        while tortoise:
            p = tortoise.next
            tortoise.next = right
            right = tortoise
            tortoise = p

        left = node
        while left is not None and right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

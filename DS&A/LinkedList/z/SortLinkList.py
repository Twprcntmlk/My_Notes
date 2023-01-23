
def sortList(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    return self.merge(*list(map(self.sortList, self.split(head))))

def split(self, head):
    fast = slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    slow.next, slow = None, slow.next
    return head, slow

def merge(self, left, right):
    dummy = p = ListNode()
    while left and right:
        if left.val <= right.val:
            p.next, left, p.next.next = left, left.next, None
        else:
            p.next, right, p.next.next = right, right.next, None
        p = p.next
    p.next = left or right
    return dummy.next

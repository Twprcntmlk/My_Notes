#Time Complexity: O(N)where N is the number of nodes in the linked list.
#Space Complexity: O(N). If we look closely, we have the recursion stack and we also have the space complexity
def copyRandomList(head):
    seen = defaultdict()#default value is None
    hold = Node(-1, None, None)
    temp = hold

    while head:
        if seen.get(head, None):
            temp.next = seen[head]
        else:
            temp.next = Node(head.val)
            seen[head] = temp.next
        temp = temp.next
        if head.random:
            if seen.get(head.random , None):
                temp.random = seen[head.random]
            else:
                temp.random = Node(head.random.val)
                seen[head.random] = temp.random
        head = head.next

    return hold.next

#https://leetcode.com/problems/copy-list-with-random-pointer/submissions/

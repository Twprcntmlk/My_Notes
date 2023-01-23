# Time complexity: O(max(m,n))
# Space complexity: O(1)

def reverseList(head):
        last = None
        while head:
            temp = head.next
            head.next = last
            last = head
            head = temp
        return last

def addTwoNumbers(List1, List2):
    # reverse lists
    List1 = reverseList(List1)
    List2 = reverseList(List2)

    head = None
    carry = 0
    while List1 or List2:
        # get the current values
        x1 = List1.val if List1 else 0
        x2 = List2.val if List2 else 0

        # current sum and carry
        val = (carry + x1 + x2) % 10
        carry = (carry + x1 + x2) // 10

        # update the result: add to front
        curr = ListNode(val)
        curr.next = head
        head = curr

        # move to the next elements in the lists
        List1 = List1.next if List1 else None
        List2 = List2.next if List2 else None

    if carry:
        curr = ListNode(carry)
        curr.next = head
        head = curr

    return head

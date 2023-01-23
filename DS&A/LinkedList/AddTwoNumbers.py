# Time complexity: O(max(l1,l2))
# Space complexity: O(max(l1,l2)) + possible carry (1)

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(l1, l2):
    newLL = ListNode()
    carry = 0
    result = newLL
    while (l1 or l2 or carry):
        if l1:
            newLL.val += l1.val
            l1 = l1.next
        if l2:
            newLL.val += l2.val
            l2 = l2.next
        # if we have a carry add it
        newLL.val += carry
        #if the sum is > 9 hold a carry
        if newLL.val > 9:
            newLL.val %= 10
            carry = 1
        else:
            carry = 0
        #if more node newLL.next add then newNode to append to and repeat
        if (l1 or l2 or carry):
            next3 = ListNode()
            newLL.next = next3
            newLL = next3
    return result

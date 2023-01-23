Iterative : Time Complexity O(N) , Space Complexity O(1)

def reverseList(head):
        hold = None

        temp = head

        while temp:
            node = temp.next
            temp.next = hold
            hold = temp
            temp = node

        return hold

Recursive: Time Complexity O(N) , Space Complexity O(N)

def reverseList(head):
        if head == None:
            return None

        newHead = head
        if head.next:
            newHead= self.reverseList(head.next)
            head.next.next=head
        head.next= None
        return newHead

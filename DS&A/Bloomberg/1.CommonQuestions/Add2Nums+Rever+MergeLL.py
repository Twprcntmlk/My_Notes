# Time complexity: O(max(m,n))
# Space complexity: O(max(m,n))
def addTwoNumbers(List1, List2):

    #     def reverseList(head):
    #         last = None
    #         while head:
    #             temp = head.next
    #             head.next = last
    #             last = head
    #             head = temp
    #         return last

    #     List1 = reverseList(List1)
    #     List2 = reverseList(List2)

    List3 = ListNode()
    carryOver = 0
    result = List3

    while List1 or List2 or carryOver:
        if List1:
            List3.val += List1.val
            List1 = List1.next
        if List2:
            List3.val += List2.val
            List2 = List2.next
        #
        List3.val += carryOver
        #
        if List3.val > 9:
            List3.val %= 10
            carryOver = 1
        else:
            carryOver = 0
        ## take care of left over
        if List1 or List2 or carryOver:
            next3 = ListNode()
            List3.next = next3
            List3 = next3
    return result #reverseList(result)

#Merge Two LinkList###############################################
    def MergeLL( ListOne, ListTwo):
        if ListOne is None and ListTwo:
            return ListTwo
        elif ListTwo is None and ListOne:
            return ListOne
        elif ListTwo is None and ListOne is None:
            return None
        res=LLNode(0,None)
        temp=res

        while ListOne and ListTwo:
            if ListOne.val > ListTwo.val:
                temp.next=ListTwo
                ListTwo=ListTwo.next
            elif ListOne.val < ListTwo.val:
                temp.next=ListOne
                ListOne=ListOne.next
            else:
                temp.next=ListOne
                ListTwo=ListTwo.next
                ListOne=ListOne.next
            temp=temp.next

        if ListOne :
            temp.next=ListOne
            temp=temp.next

        if ListTwo :
            temp.next=ListTwo
            temp=temp.next
        return res.next

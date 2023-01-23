# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, ll0, ll1):
        if ll0 is None and ll1:
            return ll1
        elif ll1 is None and ll0:
            return ll0
        elif ll1 is None and ll0 is None:
            return None
        res=LLNode(0,None)
        temp=res

        while ll0 and ll1:
            if ll0.val > ll1.val:
                temp.next=ll1
                ll1=ll1.next
            elif ll0.val < ll1.val:
                temp.next=ll0
                ll0=ll0.next
            else:
                temp.next=ll0
                ll1=ll1.next
                ll0=ll0.next
            temp=temp.next

        if ll0 :
            temp.next=ll0
            temp=temp.next

        if ll1 :
            temp.next=ll1
            temp=temp.next
        return res.next

 # O(nlog(n)) time | O(k) space
# class ListNode:
#     def __init__(self, val=0, n=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop, heapify;

def mergeKLists(lists):
        dummy = currNode = ListNode()
        nodeList = [(head.val, idx) for idx, head in enumerate(lists) if head]
        heapify(nodeList)
        while nodeList:
            node, idx = heappop(nodeList)
            currNode.next = lists[idx] #lists[idx]==node
            currNode = currNode.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heappush(nodeList, (lists[idx].val, idx))
        return dummy.next

# Time Complexity: O(N)# Space Complexity: O(N)
def flattenBITREE(self, head: 'Node') -> 'Node':
    if not head:
        return
    stack=[head]
    temp=Node(0,None,None,None)
    curr=temp
    while stack:
        node=stack.pop()
        curr.next = node
        node.prev = curr
        if node.next:
            stack.append(node.next)
        if node.child:
            stack.append(node.child)
            node.child=None
        curr=curr.next

    temp.next.prev = None
    return temp.next
###############################################################################
# Time Complexity: O(N)# Space Complexity: O(N)
def flattenStack(self, head: 'Node'):
    stack=[]
    temp = head
    while temp:
        if temp.child:
            if temp.next:
                stack.append(temp.next)
            temp.next=temp.child
            temp.child.prev=temp
            temp.child=None
        #otherwise you might hit NONE
        elif temp.child is None and temp.next is None:
            break
        temp=temp.next

    while stack:
        node=stack.pop()
        temp.next=node
        node.prev = temp
        while temp.next:
            temp=temp.next
    return head
#####################################################################################
def flattenRecusive(self, head: 'Node'):
    def dfs(head):
        temp = head
        currNode = temp
        while currNode:
            if currNode.child:
                currNode.child.temp = currNode,
                currNodenext = currNode.next
                currNode.next = currNode.child
                currNode.child = None
                currNode = dfs(currNode.next)
                currNode.next = currNodenext
                if currNode.next:
                    currNode.next.temp = currNode
            currNode = currNode.next
            temp = currNode
        return temp

    dfs(head)
    return head

#VARIATION#######################################################
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def flattenSTRAIGHT(head):
    if head == None:
        return None

    temp = head
    while temp:
        if temp.child:
            #hold that location
            temp2 = temp
            while temp2.next: # use temp2 to continue
                temp2 = temp2.next # get to the end
            #connect with the temp i left behind
            temp2.next = temp.child
            temp.child.prev = temp2
            temp.child = None
        temp = temp.next

    return head;

# Time complexity : O(1)
# Space complexity : O(N)
from collections import OrderedDict # combines behind both hashmap and linked list.
class LRUCache:
    def __init__(self):
        self.cache = OrderedDict()

    def get(self):
        if url not in self.cache :
            return -1
        else:
            self.cache.move_to_end(key, last = False) #last=True
            return result


    def put(self, url):
        if url in self.cache:
            self.cache.move_to_end(url, last = False)

        else:
            self.cache[url] = value
            self.cache.move_to_end(url, last = False)



        # if len(self) > self.cache:
        #     return self.popitem(last = False) #Makes LIFO order

# Approach 2: Hashmap + DoubleLinkedList########################################################
# Time complexity : O(1)
# Space complexity : O(cache of dict)
class DLLNode():
    def __init__(self, key, val):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache():
    def __init__(self):
        self.cache = {}
        self.head, self.tail = DLLNode(), DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self):
        # node = self.cache.get(key, None)
        if not node:
            return -1
        return

    def put(self, url):
        node = self.cache.get(url)

        if not node:
            newNode = DLLNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

        else:
            # update the value and move to head
            node.value = value
            self._remove_node(node)
            self._add_node(node)

        return self.head.next

    #################################################################################
    def _add_node(self, node): #Always add the new node right after head.
        formerNextNode = self.head.next
        self.head.next=node
        node.prev = self.head
        node.next = formerNextNode
        formerNextNode.prev = node

    def _remove_node(self, node):# Remove an existing node from the linked list.
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    # def _pop_tail(self):#Pop the current tail.
    #     res = self.tail.prev
    #     self._remove_node(res)
    #     return res
############################################################################################

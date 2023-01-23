#Time Complexity: O()
#Space Complexity: O()
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
class HashTable:
    def __init__(self):
        self.hashmap = [None for i in range(1001)]

    def find_index(self, key):
        return key % 1001

    def find(self, key, node):
        prev = None
        cur = node
        while cur and cur.key != key:
            prev = cur
            cur = cur.next
        return prev

    def put(self, key, value):
        index = self.find_index(key)
        if self.hashmap[index] is None:
            self.hashmap[index] = Node()
        node = self.hashmap[index]
        node = self.find(key, node)
        if node.next:
            node.next.value = value
        else:
            node.next = Node(key, value)

    def get(self, key):
        index = self.find_index(key)
        if self.hashmap[index] is None:
            return -1
        node = self.hashmap[index]
        node = self.find(key, node)
        if node.next:
            return node.next.value
        else:
            return -1

    def remove(self, key):
        index = self.find_index(key)
        if self.hashmap[index] is None:
            return
        node = self.hashmap[index]
        node = self.find(key, node)
        if node.next:
            node.next = node.next.next
        else:
            return

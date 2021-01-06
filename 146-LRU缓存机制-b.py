class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2node = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        else:
            self.fracture(key)
            self.move_to_head(key)

        return self.key2node[key].val

    def put(self, key: int, value: int) -> None:
        if len(self.key2node) == self.capacity and key not in self.key2node:
            rm_key = self.tail.prev.key
            self.fracture(rm_key)
            self.key2node[rm_key].next = self.key2node[rm_key].prev = None
            del self.key2node[rm_key]
        if key in self.key2node:
            self.key2node[key].val = value
            self.fracture(key)
        else:
            self.key2node[key] = Node(key, value)
        self.move_to_head(key)

    def move_to_head(self, key):
        self.key2node[key].next = self.head.next
        self.key2node[key].prev = self.head
        self.head.next.prev = self.key2node[key]
        self.head.next = self.key2node[key]

    def fracture(self, key):
        self.key2node[key].prev.next = self.key2node[key].next
        self.key2node[key].next.prev = self.key2node[key].prev

    def print_node(self):
        cur_node = self.head.next
        while cur_node != self.tail:
            print(cur_node.key, cur_node.val)
            cur_node = cur_node.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.order = []

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.visit(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            rm_key = self.order.pop(0)
            del self.cache[rm_key]
        self.cache[key] = value
        self.visit(key)

    def visit(self, key):
        for i in range(len(self.order)):
            if self.order[i] == key:
                del self.order[i]
                break
        self.order.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

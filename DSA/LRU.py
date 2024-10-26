class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        new_node = Node(key, value)
        self._add_to_head(new_node)
        self.cache[key] = new_node
        
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

# Example usage:
lru_cache = LRUCache(2)
lru_cache.put(1, 1)        # cache is {1=1}
lru_cache.put(2, 2)        # cache is {1=1, 2=2}
print(lru_cache.get(1))    # returns 1
lru_cache.put(3, 3)        # evicts key 2, cache is {1=1, 3=3}
print(lru_cache.get(2))    # returns -1 (not found)
lru_cache.put(4, 4)        # evicts key 1, cache is {4=4, 3=3}
print(lru_cache.get(1))    # returns -1 (not found)
print(lru_cache.get(3))    # returns 3
print(lru_cache.get(4))    # returns 4

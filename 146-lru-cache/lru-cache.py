class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        
        # Dummy head and tail
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node: ListNode):
        # Always add node right after head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: ListNode):
        # Remove node from its current position
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node: ListNode):
        self._remove(node)
        self._add(node)

    def _pop_tail(self):
        # Remove the last node before tail
        lru_node = self.tail.prev
        self._remove(lru_node)
        return lru_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self._add(node)
            self.size += 1

            if self.size > self.capacity:
                # Evict LRU (tail.prev)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
                self.size -= 1
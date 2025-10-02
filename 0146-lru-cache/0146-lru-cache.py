class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ht = {}   # key -> node
        # Dummy head and tail
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove node from the linked list
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Add node right after head (MRU position)
    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.ht:
            return -1
        node = self.ht[key]
        self._remove(node)
        self._add(node)  # move to MRU
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.ht:
            # Update value & move to MRU
            node = self.ht[key]
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            if len(self.ht) == self.capacity:
                # Remove LRU
                lru = self.tail.prev
                self._remove(lru)
                del self.ht[lru.key]
            # Insert new node at MRU
            node = ListNode(key, value)
            self.ht[key] = node
            self._add(node)

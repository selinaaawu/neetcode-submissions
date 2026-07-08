class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity     # max capacity
        self.cache = {}         # maps key -> node

        # dummy left/right nodes make insert/remove logic cleaner
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right     # links left to right
        self.right.prev = self.left     # links right to left

    
    def remove(self, node):
        # remove node from prev/next pointers
        before, after = node.prev, node.next
        before.next = after
        after.prev = before

    
    def insert(self, node):
        # always insert rightmost 
        before, after = self.right.prev, self.right
        before.next = after.prev = node
        node.prev = before
        node.next = after
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])    # remove node from cache
            self.insert(self.cache[key])    # insert node at right (most recently used)
            return self.cache[key].val      # return value
        return -1
        

    def put(self, key: int, value: int) -> None:
        # if key exists, remove from linked list
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)      # create/update key/value pair
        self.insert(self.cache[key])            # insert node at right (most recently used)
        
        # if at capacity, remove leftmost node
        if len(self.cache) > self.cap:
            lru = self.left.next                # least recently used node
            self.remove(lru)                    # remove lru node
            del self.cache[lru.key]             # delete lru node from cache

class ListNode:
    def __init__(self, val=0, prev = None, next=None):
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    #WORKS BUT SCALES POORLY
    def __init__(self, capacity: int):
        self.countSize = 0
        self.maxSize = capacity
        self.hashMapValues = {}
        self.head = ListNode(0)
        self.tail = self.head

    def get(self, key: int) -> int:
        if hash(key) in self.hashMapValues:
            self.updateValue(key)

        print(self.hashMapValues.get(hash(key), -1))
        return self.hashMapValues.get(hash(key), -1)

    def put(self, key: int, value: int) -> None:
        if hash(key) in self.hashMapValues:
            self.updateValue(key)
            self.hashMapValues[hash(key)] = value
            return
        
        if self.countSize == 0:
            self.head = self.tail = ListNode(hash(key), None)
            self.hashMapValues[hash(key)] = value
            self.countSize += 1

        elif self.countSize < self.maxSize :
            self.hashMapValues[hash(key)] = value
            self.tail.next = ListNode(hash(key), None)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.countSize += 1
            
        else:
            self.hashMapValues[hash(key)] = value
            self.tail.next = ListNode(hash(key), None)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.hashMapValues.pop(self.head.val)
            self.head = self.head.next


    def updateValue(self, key):
        ## One element or last element -> do nothing
        if self.countSize == 1 or self.tail.val == hash(key):
            pass
        ## Element is the head -> shift it to last place
        elif self.head.val == hash(key):
            self.head = self.head.next
            self.tail.next = ListNode(hash(key), None)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        ## Element is between the head and the tail -> shift it to last place
        else:
            cur = self.head
            while cur.next:
                if cur.next.val == hash(key):
                    cur.next = cur.next.next
                cur = cur.next
            self.tail.next = ListNode(hash(key), None)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next


lRUCache = LRUCache(3)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.put(3, 3)
lRUCache.put(4, 4)
lRUCache.get(4)
lRUCache.get(3)
lRUCache.get(2) 
lRUCache.get(1)
lRUCache.put(5, 5)
lRUCache.get(1)
lRUCache.get(2)
lRUCache.get(3)
lRUCache.get(4)
lRUCache.get(5)
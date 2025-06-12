class ListNode:
    def __init__(self, val=[], prev = None, next=None):
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.countSize = 0
        self.maxSize = capacity
        self.hashMapValues = {}
        self.head = ListNode(0)
        self.tail = self.head

    def get(self, key: int) -> int:
        if key in self.hashMapValues:
            self.updateValue(key)
            print(self.hashMapValues[key].val[1])
            return self.hashMapValues[key].val[1]
        
        else:
            print(-1)
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMapValues:
            self.hashMapValues[key].val[1] = value
            self.updateValue(key)
            #self.hashMapValues[key] = value
            return
        
        if self.countSize == 0:
            self.head = self.tail = ListNode([key,value], None)
            self.hashMapValues[key] = self.tail
            self.countSize += 1

        elif self.countSize < self.maxSize :
            self.tail.next = ListNode([key,value], None)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.hashMapValues[key] = self.tail
            self.countSize += 1
            
        else:
            self.tail.next = ListNode([key,value], None)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.hashMapValues.pop(self.head.val[0]) # type: ignore
            self.head = self.head.next # type: ignore
            self.head.prev = None # type: ignore
            self.hashMapValues[key] = self.tail


    def updateValue(self, key):
        ## One element or last element -> do nothing
        if self.countSize == 1 or self.tail == self.hashMapValues[key]:
            pass
        ## Element is the head -> shift it to last place
        elif self.head.val[0] == key:# type: ignore
            value = self.head.val[1]# type: ignore
            self.head = self.head.next# type: ignore
            self.head.prev = None# type: ignore
            self.tail.next = ListNode([key,value], None)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.hashMapValues[key] = self.tail
        ## Element is between the head and the tail -> shift it to last place
        else:
            elem = self.hashMapValues[key]
            value = elem.val[1]
            elem.prev.next = elem.next
            elem.next.prev = elem.prev
            self.tail.next = ListNode([key,value], None)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.hashMapValues[key] = self.tail

'''
lRUCache = LRUCache(3)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.put(3, 3)
lRUCache.put(4, 5)
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
'''

lRUCache = LRUCache(2)
lRUCache.put(2, 1)
lRUCache.put(2, 2)
lRUCache.get(2)
lRUCache.put(1, 1)
lRUCache.put(4, 1)
lRUCache.get(2)
# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res
        smallestNode = ListNode()

        #Remove empty lists
        noneCounter = 0
        for head in lists:
            if not head:
                noneCounter += 1
        while noneCounter > 0:
            lists.remove(None)
            noneCounter -= 1

        smallestPointer = 0
        while(lists):
            count = 0
            smallestValue = float('inf')
            for head in lists:
                if head.val < smallestValue:
                    smallestValue = head.val
                    smallestNode = head
                    smallestPointer = count
                count += 1
            dummy.next = smallestNode
            dummy = dummy.next
            lists[smallestPointer] = lists[smallestPointer].next
            if not lists[smallestPointer]:
                lists.remove(None)

        return res.next
            
        
a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)

b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)

c = ListNode(2)
c.next = ListNode(6)

Solution().mergeKLists([a,b,c])
Solution().mergeKLists([None, None])
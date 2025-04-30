# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseGroup(head: Optional[ListNode]) -> Optional[ListNode]:
            stack = []
            dummy = ListNode(0)
            res = dummy
            while head:
                stack.append(head)
                head = head.next

            while stack:
                dummy.next = stack.pop()
                dummy=dummy.next
            dummy.next = None
            return res.next
        

        if k == 1:
            return head
        pointer = head
        numElem = 0
        while pointer:
            pointer = pointer.next
            numElem += 1

        dummy = ListNode(0)
        res = dummy
        
        pointer = head
        cur = head
        saved = head
        i = 0
        while i < int(numElem/k):
            counter = 1
            while counter <k:
                cur = cur.next
                counter +=1
            saved = cur.next
            cur.next = None
            dummy.next = reverseGroup(pointer)
            while dummy.next:
                dummy = dummy.next
            pointer = saved
            cur = saved
            i+=1        
        dummy.next = saved
        return res.next



    def printHelper(self, head: Optional[ListNode]):
        while head:
            print(head.val)
            head = head.next


l1 = ListNode(1)

l1.next = ListNode(2)

l1.next.next = ListNode(3)

l1.next.next.next = ListNode(4)

l1.next.next.next.next = ListNode(5)

Solution().printHelper(Solution().reverseKGroup(l1, 2))

Solution().printHelper(Solution().reverseKGroup(l1, 3))
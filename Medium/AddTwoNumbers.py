# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addi = 0
        dummy = ListNode()
        result = dummy
        while l1 or l2:
            res = (l1.val if l1 else 0) + (l2.val if l2 else 0) + addi
            addi = 0
            if res >= 10:
                addi = 1
                res -= 10
            dummy.next = ListNode(res)
            dummy = dummy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if addi == 1:
            dummy.next = ListNode(1)

        return result.next
    

l1 = ListNode(9)
l1.next = ListNode(9)

l1.next.next = ListNode(9)

l1.next.next.next = ListNode(9)

l1.next.next.next.next = ListNode(9)

l1.next.next.next.next.next = ListNode(9)


l2 = ListNode(9)
l2.next = ListNode(9)

l2.next.next = ListNode(9)

l2.next.next.next = ListNode(9)

l2.next.next.next.next = ListNode(9)

l2.next.next.next.next.next = ListNode(9)
resu = (Solution().addTwoNumbers(l1, l2))
print(resu.val)
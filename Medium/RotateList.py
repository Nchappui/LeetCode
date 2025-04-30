# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head
        total = 1
        while temp.next:
            temp = temp.next
            total += 1
        temp.next = head
        k = k % total
        
        for _ in range(total-k-1):
            head = head.next
        res = head.next
        head.next = None

        return res

        
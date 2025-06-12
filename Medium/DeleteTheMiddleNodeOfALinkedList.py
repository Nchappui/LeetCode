# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        faster = slower = ListNode()
        faster.next = slower.next = head

        while(faster.next and faster.next.next):
            slower = slower.next # type: ignore
            faster = faster.next.next

        slower.next = slower.next.next # type: ignore


        return head
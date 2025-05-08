# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        while tail.next:
            tail = tail.next
        dummy = head
        while dummy != tail:
            if dummy.val > dummy.next.val:
                NotImplemented
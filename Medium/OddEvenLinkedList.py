# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        dummy1 = head
        dummy2 = temp = head.next
        while dummy1.next and dummy1.next.next:
            dummy1.next = dummy1.next.next
            dummy1 = dummy1.next
            dummy2.next = dummy1.next
            dummy2 = dummy2.next
        dummy1.next = temp
        return head
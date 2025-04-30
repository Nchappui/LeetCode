# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pointer = head
        count = 1
        stack = []
        while pointer:
            if left <= count <= right:
                stack.append(pointer.val)
            count += 1
            pointer = pointer.next
            

        count = 1
        dummy = ListNode()
        result = dummy
        while head:
            if left <= count <= right:
                dummy.next = ListNode(stack.pop())
            else:
                dummy.next = head
            dummy = dummy.next
            head = head.next
            count += 1

        return result.next
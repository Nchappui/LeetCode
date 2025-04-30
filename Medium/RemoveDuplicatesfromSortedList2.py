# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = ListNode(-101)
        res = pointer
        toDelete = set()
        if not head or not head.next:
            return head
        while head.next:
            if pointer.val < head.val < head.next.val and head.val not in toDelete:
                pointer.next = head
                pointer=pointer.next
                head = head.next
            else:
                toDelete.add(head.val)
                head = head.next

        if head.val not in toDelete:
            pointer.next = head
        else: pointer.next = None
    
    def printHelper(self, head: Optional[ListNode]):
        while head:
            print(head.val)
            head = head.next


l1 = ListNode(1)

l1.next = ListNode(2)

l1.next.next = ListNode(3)

l1.next.next.next = ListNode(3)

l1.next.next.next.next = ListNode(4)

l1.next.next.next.next.next = ListNode(4)

l1.next.next.next.next.next.next = ListNode(5)

Solution().printHelper(Solution().deleteDuplicates(l1))
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:

    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
            result = ListNode()
            pointer = result
            while head1 and head2:
                if head1.val < head2.val :
                    pointer.next = head1
                    head1 = head1.next
                else:
                    pointer.next = head2
                    head2 = head2.next
                pointer = pointer.next
            if head1:
                pointer.next = head1
            else:
                pointer.next = head2
            return result.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        dummy, tail1 = head, ListNode(0, head)
        while dummy and dummy.next:
                dummy = dummy.next.next
                tail1 = tail1.next
        newHead = tail1.next
        tail1.next = None

        sortedHead = self.sortList(head)
        sortedHead2 = self.sortList(newHead)
        return self.merge(sortedHead, sortedHead2)
    
temp = ListNode(-1)
temp.next = ListNode(5)
temp.next.next = ListNode(3)
temp.next.next.next = ListNode(4)
temp.next.next.next.next = ListNode(0)
Solution().sortList(temp)

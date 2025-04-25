# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1, pointer2= list1, list2
        dummy = ListNode()
        res = dummy
        while pointer1 and pointer2:
            if pointer1.val > pointer2.val:
                res.next = pointer2
                pointer2=pointer2.next
            else :
                res.next = pointer1
                pointer1=pointer1.next

            res = res.next

        if pointer1:
            res.next = pointer1

        if pointer2:
            res.next = pointer2

        return dummy.next

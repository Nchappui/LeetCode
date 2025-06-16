# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = head
        stack = []
        while dummy:
            stack.append(dummy.val)
            dummy = dummy.next
        n = len(stack)
        res = 0
        for i in range(n//2):
            curr = stack[i] + stack[n-1-i]
            res = max(curr, res)
        return res
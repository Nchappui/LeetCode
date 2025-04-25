# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        smallestValue = float('inf')
        smallestNode = ListNode()
        while(lists):
            for list in lists:
                if list.val < smallestValue:
                    smallestValue = list.val
                    smallestNode = list

            cur.next = smallestNode
            for list in lists:
                if list == smallestNode:
                    list=list.next
                if list : 
                    continue
                else:
                    lists.remove(list)
        return cur.next
            
        

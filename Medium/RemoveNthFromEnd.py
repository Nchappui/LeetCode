from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEndTest(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res
        def traverse(currentNode : ListNode, previousNNode : ListNode, counter:int, n):
            if (currentNode.next is None):
                previousNNode.next=previousNNode.next.next
            elif counter<n :
                traverse(currentNode.next, previousNNode, counter+1, n)
            else:
                traverse(currentNode.next, previousNNode.next, counter, n)

        
        traverse(head, dummy, 0, n)
        return res
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return res.next
    
print(Solution().removeNthFromEnd([1,2,3,4,5],2))
    


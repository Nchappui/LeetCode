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



    def removeNthFromEndAgain(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        res = dummy

        cur = head
        count = 0 
        while cur:
            cur = cur.next
            count += 1
        n = count - n

        if count == 1:
            return None 

        for _ in range(n):
            dummy = dummy.next
        if dummy.next and dummy.next.next:
            dummy.next=dummy.next.next
        else : dummy.next = None

        return res.next

    
    def printHelper(self, head: Optional[ListNode]):
        while head:
            print(head.val)
            head = head.next


l1 = ListNode(1)

l1.next = ListNode(2)

#l1.next.next = ListNode(3)

#l1.next.next.next = ListNode(4)

#l1.next.next.next.next = ListNode(5)

Solution().printHelper(Solution().removeNthFromEndAgain(l1,2))
    


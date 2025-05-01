from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallerPointer = ListNode(0)
        beginSmaller = smallerPointer
        biggerPointer = ListNode(0)
        beginBigger = biggerPointer

        while head:
            if head.val  < x:
                smallerPointer.next = head
                smallerPointer = smallerPointer.next
            else:
                biggerPointer.next = head
                biggerPointer = biggerPointer.next

            head = head.next
        biggerPointer.next = None
        smallerPointer.next = beginBigger.next

        return beginSmaller.next

    def printHelper(self, head: Optional[ListNode]):
        while head:
            print(head.val)
            head = head.next

l1 = ListNode(1)

l1.next = ListNode(4)

l1.next.next = ListNode(3)

l1.next.next.next = ListNode(2)

l1.next.next.next.next = ListNode(5)

l1.next.next.next.next.next = ListNode(2)


Solution().printHelper(Solution().partition(l1,4))
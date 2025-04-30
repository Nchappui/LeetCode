class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        result = dummy

        while list1 or list2:
            if not list1:
                dummy.next = ListNode(list2.val)
                list2 = list2.next

            elif not list2:
                dummy.next = ListNode(list1.val)
                list1 = list1.next
            
            elif list1.val<list2.val :
                dummy.next = ListNode(list1.val)
                list1 = list1.next

            else:
                dummy.next = ListNode(list2.val)
                list2 = list2.next

            dummy = dummy.next
        
        return result.next
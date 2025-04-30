
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        pointer = head
        hashMap = {None:None} 

        while pointer:
            hashMap[pointer] = Node(pointer.val)
            pointer = pointer.next

        pointer = head
        while pointer:
            copy = hashMap[pointer]
            copy.next = hashMap[pointer.next]
            copy.random = hashMap[pointer.random]
            pointer = pointer.next

        return hashMap[head]


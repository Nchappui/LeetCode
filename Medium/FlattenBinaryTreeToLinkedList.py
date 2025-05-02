# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        previousNode = None
        def invertBFS(root):
            nonlocal previousNode
            if not root:
                return
            invertBFS(root.right)
            invertBFS(root.left)
            root.right = previousNode
            root.left = None
            previousNode = root
        invertBFS(root)
        '''
        def BFS(root):
            if not root:
                return
            rL = root.left
            rR = root.right
            root.left = root.right = None
            order.append(root)
            BFS(rL)
            BFS(rR)
        BFS(root)
        for i in range(len(order)-1):
            order[i].right = order[i+1]
        if order:
            order[len(order)-1] = None

        '''
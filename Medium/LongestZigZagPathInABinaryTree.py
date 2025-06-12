# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxLen = 0
        if not root:
            return 0
        
        def zigZag(movedLeft, currLen, node):
            nonlocal maxLen
            if not node:
                maxLen = max(maxLen, currLen-1)
                return
            if movedLeft:
                zigZag(True, 1, node.left)
                zigZag(False, currLen+1, node.right)
            else:
                zigZag(False, 1, node.right)
                zigZag(True, currLen+1, node.left)

        zigZag(True, 1, root.left)
        zigZag(False, 1, root.right)
        return maxLen
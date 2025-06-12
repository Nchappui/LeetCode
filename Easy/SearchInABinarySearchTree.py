# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = None
        def traverse(node):
            nonlocal res
            if not node or res:
                return
            if node.val == val:
                res = node
                return
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return res
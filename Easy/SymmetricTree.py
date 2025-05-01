# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    
        def invertTree(root: Optional[TreeNode]):
            if not root:
                return
            root.right, root.left = invertTree(root.left), invertTree(root.right)
            return root
        
        def isSame(l :Optional[TreeNode], r :Optional[TreeNode]):
            if l and not r or not l and r:
                return False
            elif not l and not r:
                return True
            else:
                return l.val == r.val and isSame(l.left, r.left) and isSame(l.right, r.right)

        root.right = invertTree(root.right)

        if not root.left and root.right or root.left and not root.right:
            return False
        return isSame(root.left, root.right)

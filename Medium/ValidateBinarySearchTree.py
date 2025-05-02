# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        previousVal = float('-inf')
        result = True
        def inOrder(root):
            nonlocal previousVal
            nonlocal result
            if not root:
                return
            inOrder(root.left)
            if root.val <= previousVal:
                result = False
            previousVal = root.val
            inOrder(root.right)

        inOrder(root)
        return result
            


    '''
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root):
            if not root:
                return
            if not root.left and root.right:
                return root.val < root.right.val and bst(root.right)
            elif root.left and not root.right:
                return root.left.val < root.val and bst(root.left)
            elif not root.left and not root.right:
                return True
            else:
                return root.left.val < root.val < root.right.val and bst(root.left) and bst(root.right)
            
        return(bst(root))
    '''    
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None
        def inOrder(root):
            nonlocal k
            nonlocal result
            if not root or result:
                return
            inOrder(root.left)
            if k == 1:
                k = k - 1
                result = root.val
                return
            k = k - 1
            inOrder(root.right)
        inOrder(root)
        return result# type: ignore
        

    '''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        def dfs(root):
            if not root:
                return
            stack.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        stack.sort()
        return stack[k-1]
        '''
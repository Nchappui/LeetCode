# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        def dfs(root):
            if not root:
                return
            stack.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        stack.sort()
        mini = float('inf')
        for i in range(len(stack)-1):
            mini = min(stack[i+1] - stack[i], mini)

        return mini
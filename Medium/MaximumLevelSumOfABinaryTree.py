# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        values = []
        def traverse(root, level):
            if not root:
                return
            if len(values) < level:
                values.append(root.val)
            else:
                values[level-1]+=root.val
            traverse(root.left, level+1)
            traverse(root.right, level+1)
        traverse(root,1)
        max = values[0]
        res = 1
        for i in range(len(values)):
            if values[i] > max:
                res = i+1
                max = values[i]
        return res
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum = 0
        def sumBranch(root, currentSum):
            if not root:
                return
            elif not root.left and not root.right:
                nonlocal sum
                currentSum *= 10
                currentSum += root.val
                sum += currentSum
            else:
                currentSum *= 10
                currentSum += root.val
                sumBranch(root.left, currentSum)
                sumBranch(root.right, currentSum)

        sumBranch(root, 0)
        return sum
            
# Definition for a binary tree node.
import math
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        
        middle = len(nums) // 2
        tree = TreeNode(nums[middle])
        tree.left = self.sortedArrayToBST(nums[:middle])
        tree.right = self.sortedArrayToBST(nums[middle + 1:])

        return tree

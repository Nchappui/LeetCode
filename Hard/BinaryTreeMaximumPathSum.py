# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def maxDownPathSum(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val if root.val > 0 else 0
        else : 
            return max(self.maxDownPathSum(root.left), self.maxDownPathSum(root.right))+ root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        if not root.left and root.right:
            return max (max(self.maxDownPathSum(root.left),0) +max(self.maxDownPathSum(root.right),0) + root.val,
                        self.maxPathSum(root.right))
        elif root.left and not root.right:
            return max (max(self.maxDownPathSum(root.left),0) +max(self.maxDownPathSum(root.right),0) + root.val,
                        self.maxPathSum(root.left))
        else:
            return max (max(self.maxDownPathSum(root.left),0) +max(self.maxDownPathSum(root.right),0) + root.val,
                        self.maxPathSum(root.left),
                        self.maxPathSum(root.right))
       
temp = TreeNode(1)
temp.left = TreeNode(-2)
temp.right = TreeNode(-3)
temp.left.left = TreeNode(1)
temp.left.right = TreeNode(3)
temp.right.left = TreeNode(-2)
temp.left.left.left = TreeNode(-1)

print(Solution().maxPathSum(temp))
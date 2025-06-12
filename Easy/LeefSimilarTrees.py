## Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1 = []
        r2 = []
        def computeLeafvalue(currNode, currStack):
            if not currNode:
                return
            if not currNode.left and not currNode.right:
                currStack.append(currNode.val)
            else:
                computeLeafvalue(currNode.left, currStack)
                computeLeafvalue(currNode.right, currStack)
        
        computeLeafvalue(root1, r1)
        computeLeafvalue(root2, r2)

        return r1 == r2
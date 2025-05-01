# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        head = postorder.pop()
        leftInorder = inorder[:inorder.index(head)]
        rightInorder = inorder[inorder.index(head)+1:]

        def build(inorder):
            if inorder:
                head = postorder.pop()
                leftInorder = inorder[:inorder.index(head)]
                rightInorder = inorder[inorder.index(head)+1:]
                rightTree = build(rightInorder)
                return TreeNode(head, build(leftInorder), rightTree)
            
        rightTree = build(rightInorder)
        return TreeNode(head, build(leftInorder), rightTree)
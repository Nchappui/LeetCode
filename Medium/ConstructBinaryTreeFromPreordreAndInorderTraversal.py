# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        head = preorder[0]
        leftInorder = inorder[:inorder.index(head)]
        rightInorder = inorder[inorder.index(head)+1:]
        leftPreorder = preorder[1:len(leftInorder)+1]
        rightPreorder = preorder[len(leftInorder)+1:]

        if leftInorder and rightInorder:
            return(TreeNode(head, self.buildTree(leftPreorder, leftInorder), self.buildTree(rightPreorder, rightInorder)))
        elif not leftInorder and rightInorder:
            return(TreeNode(head, None, self.buildTree(rightPreorder, rightInorder)))
        elif leftInorder and not rightInorder:
            return(TreeNode(head, self.buildTree(leftPreorder, leftInorder), None))
        else:
            return(TreeNode(head, None, None))
        #print(leftInorder, rightInorder, leftPreorder, rightPreorder)

        

Solution().buildTree([3,9,10,20,15,11,7], [10,9,3,11,15,20,7])
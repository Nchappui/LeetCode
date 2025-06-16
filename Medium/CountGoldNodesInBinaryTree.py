# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 1
        def traverse(node, maxElem):
            nonlocal count
            if not node:
                return
            if maxElem <= node.val:
                maxElem = node.val
                count += 1
            traverse(node.left, maxElem)
            traverse(node.right, maxElem)

        traverse(root.left, root.val)
        traverse(root.right, root.val)

        return count
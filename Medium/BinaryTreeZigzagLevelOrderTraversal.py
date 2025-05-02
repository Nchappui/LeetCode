# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = []
        def bfs(root, depth, fromRight):
            if not root:
                return
            if len(stack)<=depth:
                stack.append([])
            if fromRight:    
                stack[depth].append(root.val)
            else:
                stack[depth].insert(0, root.val)
            bfs(root.left, depth+1, not fromRight)
            bfs(root.right, depth+1, not fromRight)

        bfs(root, 0, True)
        return stack
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        stack = []
        def dfs(root, depth):
            if not root:
                return
            if len(stack)<=depth:
                stack.append([])
            stack[depth].append(root.val)
            dfs(root.left,depth+1)
            dfs(root.right, depth+1)

        dfs(root, 0)
        result = []
        for row in stack:
            result.append(sum(row)/len(row))
        return(result)
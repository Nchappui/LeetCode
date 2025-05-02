# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pointer = 0
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            self.stack.append(root.val)
            inOrder(root.right)
        inOrder(root)

    def next(self) -> int:
        val = self.stack[self.pointer]
        self.pointer += 1
        return val

    def hasNext(self) -> bool:
        return self.pointer < len(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
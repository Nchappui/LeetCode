
# Definition for a QuadTree node.
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def checkIsLeaf(self, grid: List[List[int]]) -> tuple[bool, int]:
        val = grid[0][0]
        n = len(grid)
        for x in range(n):
            for y in range(n):
                if val != grid[x][y]: return False, val
        return True, val

    def construct(self, grid: List[List[int]]) -> 'Node':

        checkGrid = self.checkIsLeaf(grid)

        if checkGrid[0]:
            return Node(checkGrid[1], True, None, None, None, None)
        n = len(grid)
        mid = n//2
        topLeft = [row[:mid] for row in grid[:mid]] 
        topRight = [row[mid:] for row in grid[:mid]]
        bottomLeft = [row[:mid] for row in grid[mid:]]
        bottomRight = [row[mid:] for row in grid[mid:]]
        
        topLeftIsLeaf = self.checkIsLeaf(topLeft)
        topRightIsLeaf = self.checkIsLeaf(topRight)
        bottomLeftIsLeaf = self.checkIsLeaf(bottomLeft)
        bottomRightIsLeaf = self.checkIsLeaf(bottomRight)

        topLeftLeaf = Node(topLeftIsLeaf[1], True, None, None, None, None) if topLeftIsLeaf[0] else self.construct(topLeft)
        topRightLeaf = Node(topRightIsLeaf[1], True, None, None, None, None) if topRightIsLeaf[0] else self.construct(topRight)
        bottomLeftLeaf = Node(bottomLeftIsLeaf[1], True, None, None, None, None) if bottomLeftIsLeaf[0] else self.construct(bottomLeft)
        bottomRightLeaf = Node(bottomRightIsLeaf[1], True, None, None, None, None) if bottomRightIsLeaf[0] else self.construct(bottomRight)
        
        result = Node (0, False, topLeftLeaf, topRightLeaf, bottomLeftLeaf, bottomRightLeaf)
        return result


Solution().construct([[1,1,1,1,0,0,0,0],
                      [1,1,1,1,0,0,0,0],
                      [1,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,1,1],
                      [1,1,1,1,0,0,0,0],
                      [1,1,1,1,0,0,0,0],
                      [1,1,1,1,0,0,0,0],
                      [1,1,1,1,0,0,0,0]])
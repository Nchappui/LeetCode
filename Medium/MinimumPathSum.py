from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if x == 0 and y == 0:
                    continue
                grid[x][y] += min(grid[x-1][y] if x > 0 else float('inf'), grid[x][y-1] if y > 0 else float('inf'))
        
        return grid[-1][-1]
    
Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])

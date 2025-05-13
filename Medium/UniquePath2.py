from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for x in range(len(obstacleGrid)):
            for y in range(len(obstacleGrid[0])):
                if obstacleGrid[x][y] == 1:
                    obstacleGrid[x][y] = 0
                    continue
                if x == 0 and y == 0:
                    obstacleGrid[x][y] = 1
                    continue
                obstacleGrid[x][y] = (obstacleGrid[x-1][y] if x > 0 else 0) + (obstacleGrid[x][y-1] if y > 0 else 0)
        
        return obstacleGrid[-1][-1]
    
Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
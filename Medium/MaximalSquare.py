from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxSquare = 0
        dpArray = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == "1":
                    dpArray[x][y] = 1 + min(dpArray[x-1 if x > 0 else 0][y],min(dpArray[x][y-1 if y > 0 else 0],dpArray[x-1 if x > 0 else 0][y-1 if y > 0 else 0]))
                    maxSquare = max(maxSquare, dpArray[x][y])
        return maxSquare**2
    
print(Solution().maximalSquare([["1","0","1","0","0"],
                                ["1","0","1","1","1"],
                                ["1","1","1","1","1"],
                                ["1","0","1","1","1"]]))
from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = defaultdict(int)
        res = 0
        for i in range(n):
            rows[str(grid[i])] += 1

        for i in range(n):
            currCol = []
            for j in range(n):
                currCol.append(grid[j][i])
                
            if str(currCol) in rows.keys():
                res += rows[str(currCol)]

        return res
    
print(Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
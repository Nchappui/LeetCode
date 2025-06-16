from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = set()
        cleanCount = 0
        rows = len(grid)
        cols = len(grid[0])
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    cleanCount += 1
                if grid[x][y] == 2:
                    rottens.add((x,y))
        if not rottens and cleanCount:
            return -1
        elif not cleanCount:
            return 0
        
        minutes = 0
        while cleanCount != 0:
            newRottens = set()
            for rotten in rottens:
                for dz in ((-1,0),(1,0),(0,-1),(0,1)):
                    x = rotten[0] + dz[0]
                    y = rotten[1] + dz[1]
                    if 0<=x<rows and 0<=y<cols and grid[x][y] == 1:
                        if (x,y) not in newRottens:
                            newRottens.add((x,y))
                            cleanCount-=1
                            grid[x][y]=2
            if not newRottens and cleanCount>0:
                return -1
            rottens = newRottens
            minutes += 1
        return minutes
    
Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
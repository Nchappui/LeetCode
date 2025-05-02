from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        totalIslands = 0
        def removeIsland(x,y):
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == "1":
                grid[x][y] = "0"
                removeIsland(x+1, y)
                removeIsland(x-1, y)
                removeIsland(x, y+1)
                removeIsland(x, y-1)
            

        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    totalIslands+= 1
                    removeIsland(x,y)
        return totalIslands
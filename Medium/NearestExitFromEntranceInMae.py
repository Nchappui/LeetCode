import math
from typing import List


class Solution:
    ### TLE
    """
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        minExit = float('inf')
        def findSmallest(current: List[int], numMoves, numCols, numRows, prevVisited):
            nonlocal minExit
            if current[0] not in range(numRows) or current[1] not in range(numCols) or maze[current[0]][current[1]] == "+" or numMoves >= minExit or current in prevVisited:
                return
            if (0 in current or current[0] == numRows-1 or current[1] == numCols-1) and numMoves>0:
                minExit = min(minExit, numMoves)
                return
            else:
                visited = prevVisited.copy()
                visited.append(current)
                for dz in [(-1,0), (1,0), (0,-1), (0,1)]:
                        newCurr = [current[0]+dz[0],current[1]+dz[1]]
                        findSmallest(newCurr, numMoves+1, numCols, numRows, visited)

        findSmallest(entrance, 0, len(maze[0]), len(maze), [])

        return minExit if minExit != float('inf') else -1 # type: ignore
    """
    ## Attention il faut marquer un node comme visité dès qu'il a été enqueue et pas lorsqu'il a été dequeue
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        numMoves = 0
        currentPoints = [entrance]
        numRows = len(maze)
        numCols = len(maze[0])
        maze[entrance[0]][entrance[1]] = '+'
        while currentPoints:
            numMoves+=1
            for point in currentPoints.copy():
                currentPoints.remove(point)
                for dz in [[-1,0], [1,0], [0,-1], [0,1]]:
                    newPoint = [point[0] + dz[0], point[1] + dz[1]]
                    if newPoint[0] in range(numRows) and newPoint[1] in range(numCols) and maze[newPoint[0]][newPoint[1]] != '+':
                        ##Valid point
                        maze[newPoint[0]][newPoint[1]] = '+'
                        if (0 in newPoint or newPoint[0] == numRows-1 or newPoint[1] == numCols-1):
                            return numMoves
                        else:
                            currentPoints.append(newPoint)
        
        return -1
    
print(Solution().nearestExit([["+",".","+","+","+","+","+"],
                              ["+",".","+",".",".",".","+"],
                              ["+",".","+",".","+",".","+"],
                              ["+",".",".",".",".",".","+"],
                              ["+","+","+","+",".","+","."]], [0,1]))
print(Solution().nearestExit([["+",".","+","+","+","+","+"],
                              ["+",".","+",".",".",".","+"],
                              ["+",".","+",".","+",".","+"],
                              ["+",".",".",".",".",".","+"],
                              ["+","+","+","+",".","+","."]], [0,1]))
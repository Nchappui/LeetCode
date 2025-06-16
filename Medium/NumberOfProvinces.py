from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        visited = set()
        visited.add(0)
        toVisit = set()
        toVisit.add(0)
        provinces = 1
        while len(visited)!= n:
            newlyvisited = set()
            for city in toVisit:
                for newCity in range(n):
                    if isConnected[city][newCity] and newCity not in visited:
                        newlyvisited.add(newCity)
                        visited.add(newCity)
            if not newlyvisited:
                provinces += 1
                toVisit.clear()
                for i in range(n):
                    if i not in visited:
                        toVisit.add(i)
                        visited.add(i)
                        break
            else:
                toVisit.clear()
                for elem in newlyvisited:
                    toVisit.add(elem)
        return provinces
    
Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
Solution().findCircleNum([[1,1,1],[1,1,1],[1,1,1]])
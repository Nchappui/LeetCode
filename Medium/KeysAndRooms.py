from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        n = len(rooms)
        visited = set()
        visited.add(0)
        toVisit = set()
        toVisit.add(0)

        while len(visited)!= n:
            newlyvisited = set()
            for room in toVisit:
                for newRoom in rooms[room]:
                    if newRoom not in visited:
                        newlyvisited.add(newRoom)
                        visited.add(newRoom)
            if not newlyvisited:
                return False
            else:
                toVisit.clear()
                for elem in newlyvisited:
                    toVisit.add(elem)
        return True
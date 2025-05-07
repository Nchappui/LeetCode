from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        flattenboard = []
        graph = {}
        ascending = False
        n = len(board)
        for i in range(n):
            ascending = not ascending
            for j in range(n):
                xCord = n-i-1
                yCord = j if ascending else n-j-1
                flattenboard.append(board[xCord][yCord])

        for i in range(n*n):
            graph.setdefault(i+1, [])
            for j in range(6):
                if i+j+1 < n*n:
                    if flattenboard[i+j+1] == -1:
                        graph[i+1].append(i+j+2)
                    else:
                        graph[i+1].append(flattenboard[i+j+1])
                

        visited = set()
        queue = [(1,0)]

        while queue:
            current, moves = queue.pop(0)

            if current == n*n:
                return moves
            if current in visited:
                continue

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, moves + 1))
            visited.add(current)

        return -1
Solution().snakesAndLadders([[-1,-1,-1,-1,-1,-1],
                             [-1,-1,-1,-1,-1,-1],
                             [-1,-1,-1,-1,-1,-1],
                             [-1,35,-1,-1,13,-1],
                             [-1,-1,-1,-1,-1,-1],
                             [-1,15,-1,-1,-1,-1]])
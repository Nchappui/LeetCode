from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        toChange = set()

        n = len(board[0])
        m = len(board)

        def checkCell(i, j, toChange, n, m):
            count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc]:
                        count += 1
            if board[i][j] :
                if count != 2 and count != 3:
                    toChange.add((i,j))
            else : 
                if count == 3: toChange.add((i,j))

        for i in range (len(board)):
            for j in range(len(board[0])):
                checkCell(i,j, toChange, n, m)
        
        for elem in toChange:
            if board[elem[0]][elem[1]] : board[elem[0]][elem[1]] = 0
            else: board[elem[0]][elem[1]] = 1
        print(board)

Solution().gameOfLife([[1,1]])
        
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
                
        def modifyRegion(x,y):
            if 0<x<m-1 and 0<y<n-1 and board[x][y] == "O":
                board[x][y] = "A"
                modifyRegion(x-1,y)
                modifyRegion(x+1,y)
                modifyRegion(x,y-1)
                modifyRegion(x,y+1)

        for i in range(n):
            if board[0][i] == "O":
                modifyRegion(1,i)
            if board[m-1][i] == "O":
                modifyRegion(m-2,i)

        for i in range(m):
            if board[i][0] == "O":
                modifyRegion(i,1)
            if board[i][n-1] == "O":
                modifyRegion(i,n-2)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j]=="O" and (board[i+1][j]=="X" or board[i-1][j]=="X" or board[i+1][j]=="X" or board[i-1][j]=="X"):
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"


Solution().solve([["O","X","X","O","X"],
                  ["X","O","O","X","O"],
                  ["X","O","X","O","X"],
                  ["O","X","O","O","O"],
                  ["X","X","O","X","O"]])
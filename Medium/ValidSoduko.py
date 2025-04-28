from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkLine(line):
            newLine = line.copy()
            newLine.sort()
            for i in range(8):
                if newLine[i] != "." and newLine[i] == newLine[i+1]:
                    return False
            return True

        ## Check rows
        for row in board:
            if not checkLine(row): return False
                
        ## Check columns
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            if not checkLine(column): return False

        ## Check boxes
        twoDArray = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                twoDArray[(i//3)*3+j//3].append(board[i][j])
        for row in twoDArray:
            if not checkLine(row): return False
        return True


print(Solution().isValidSudoku(
    [[".",".","4",".",".",".","6","3","."],
     [".",".",".",".",".",".",".",".","."],
     ["5",".",".",".",".",".",".","9","."],
     [".",".",".","5","6",".",".",".","."],
     ["4",".","3",".",".",".",".",".","1"],
     [".",".",".","7",".",".",".",".","."],
     [".",".",".","5",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."]]))
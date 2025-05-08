from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recFunc(x, y, word):
            if not word:
                return True

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newX, newY = x + dx, y + dy
                if 0<=newX<len(board) and 0 <=newY<len(board[0]):
                    if(board[newX][newY])== word[0]:
                        temp, board[newX][newY] = board[newX][newY], "_"         
                        if not recFunc(newX,newY,word[1:]):
                            board[newX][newY] = temp
                        else:
                            return True

        for x in range(len(board)):
            for y in range(len(board[0])):
                if(board[x][y])== word[0]:
                    temp, board[x][y] = board[x][y], "_"         
                    if not recFunc(x,y,word[1:]):
                        board[x][y] = temp
                    else:
                        return True
        
        return False
    
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
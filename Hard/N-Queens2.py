class Solution:
    def totalNQueens(self, n: int) -> int:
        answer = 0
        placement = []
        availableY = list(range(n))
        def isValid(queens: list[(tuple)], newQueen:tuple):
            if not queens: return True
            for x, y in queens:
                #Pas sur la même diagonale
                for i in range(1, n):
                    if newQueen == (x+i,y+i) or newQueen == (x-i,y-i) or newQueen == (x+i,y-i) or newQueen == (x-i,y+i):
                        return False
            return True
        
        def recFunc(queens, xStart):
            if len(queens) == n:
                queens.sort()
                if queens not in placement:
                    nonlocal answer
                    placement.append(queens.copy())
                    answer += 1
                return

            for j in availableY.copy():
                newQueen = (xStart,j)
                if isValid(queens, newQueen):
                    queens.append(newQueen)
                    availableY.remove(j)
                    recFunc(queens, xStart+1)
                    availableY.append(queens[-1][1])
                    queens.pop()
                        
        recFunc([], 0)
        return answer
    
print(Solution().totalNQueens(5))
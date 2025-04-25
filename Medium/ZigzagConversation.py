class Solution:
    def convert(self, s: str, numRows: int) -> str:
        twoDArray = [[""] * len(s) for _ in range(numRows)]
        colNum=0
        descending = True
        for i in range(len(s)):
            twoDArray[colNum][i] = s[i]
            if numRows == 1:
                continue
            if descending:
                colNum+=1
                if colNum == numRows-1: descending = False
            else:
                colNum-=1
                if colNum == 0: descending = True

        
        for i in range(numRows):
            twoDArray[i] = ''.join(twoDArray[i])

        return ''.join(twoDArray)

print(Solution().convert("PAYPALISHIRING", 3))
import math


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        maxi = max(a,b,c)
        bitsToCheck = math.floor(math.log2(maxi)) + 1
        binA = bin(a)
        binB = bin(b)
        binC = bin(c)
        aReached  = bReached = cReached = False
        for i in range (bitsToCheck):
            tempA = binA[-1-i] if not aReached else '0'
            tempB = binB[-1-i] if not bReached else '0'
            tempC = binC[-1-i] if not cReached else '0'
            if tempA == 'b':
                aReached = True
                tempA = '0'
            if tempB == 'b':
                bReached = True
                tempB = '0'
            if tempC == 'b':
                cReached = True
                tempC = '0'
            if tempC == '1' and tempA == '0' and tempB == '0':
                res += 1
            elif tempC == '0':
                res += 1 if tempA == '1' else 0
                res += 1 if tempB == '1' else 0    
        return res
    
Solution().minFlips(4,2,10)
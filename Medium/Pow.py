class Solution:
    def myPow(self, x: float, n: int) -> float:
        isNeg = True if n < 0 else False
        def calculatePow(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            elif n%2:
                ans = calculatePow(x, n//2)
                ans = x * ans * ans
            else:
                ans = calculatePow(x, n/2)
                ans *= ans
            return ans
        if isNeg:
            res = 1/calculatePow(x,-n)
        else:
            res = calculatePow(x,n)

        return res
    
Solution().myPow(2,10)
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def nextNumb(n):
            res = 0
            for c in str(n):
                res += int(c) * int(c)
            return res
        while (n not in seen):
            seen.add(n)
            n=nextNumb(n)
            if n == 1 :
                return True
        return False
            
Solution().isHappy(19)
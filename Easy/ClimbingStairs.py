class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        prev = 3
        prevAgain = 2
        cur = 0
        for _ in range(3,n):
            cur = prev + prevAgain
            prevAgain = prev
            prev = cur
        return cur
    
        ###FIBONNACI SOLUTION, TLE
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else :
            return self.climbStairs(n-1) + self.climbStairs(n-2)

        ###OTHER RECURSION SOLUTION, TLE
        def climbHelper(steps):
            if steps > n:
                return 0
            elif steps == n:
                return 1
            else :
                return climbHelper(steps + 1) + climbHelper(steps + 2)
            
        return climbHelper(0)
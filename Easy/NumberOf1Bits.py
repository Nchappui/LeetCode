class Solution:
    def hammingWeight(self, n: int) -> int:  
        res = 0
        for i in range(32):
            if pow(2,31-i)<=n:
                n-=pow(2,31-i)
                res += 1
        return res
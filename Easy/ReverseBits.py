class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if pow(2,31-i)<=n:
                n-=pow(2,31-i)
                res += pow(2,i)
        return res
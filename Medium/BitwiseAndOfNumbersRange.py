class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i=0
        res = right & left
        count = right-left + 1
        mask = 2**32-2
        while(pow(2,i)+1<=count):
            res &= mask
            mask <<= 1         
            i += 1
        return res

Solution().rangeBitwiseAnd(5,7)
Solution().rangeBitwiseAnd(6,7)
Solution().rangeBitwiseAnd(0,0)
Solution().rangeBitwiseAnd(1,2147483647)

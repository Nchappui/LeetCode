from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            sum = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32-1)
                num = num >> i
                sum += num & 1
            sum = sum % 3 
            ans = sum << i | ans
            
        if ans >= 2**31:
            ans -= 2**32
        return ans
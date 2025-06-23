from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = 0
        maxi = 0
        for i in range(k):
            res += nums[i]
        maxi = res
        for i in range(k,len(nums)):
            res -= nums[i-k]
            res += nums[i]
            maxi = max(res, maxi)
            
        return maxi/k
    
Solution().findMaxAverage([1,12,-5,-6,50,3], 4)
        
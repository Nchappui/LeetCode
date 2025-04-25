from typing import List


class Solution:

    ##DOUBLE FOR LOOP NOT SCALING
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for i in range(1, len(nums)+1):
            for j in range (len(nums)-i+1):
                if sum(nums[j : j+i]) >= target:
                    return i
        return 0
    
print(Solution().minSubArrayLen(15,[1,2,3,4,5]))
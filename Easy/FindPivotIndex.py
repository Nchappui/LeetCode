from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        leftcount = 0
        rightcount = sum(nums) - nums[0]
        while left < len(nums) - 1:
            if leftcount == rightcount:
                return left
            leftcount += nums[left]
            left += 1
            rightcount -= nums[left]
        if leftcount == rightcount:
                return left
        return -1
    
Solution().pivotIndex([-1, 1,2])
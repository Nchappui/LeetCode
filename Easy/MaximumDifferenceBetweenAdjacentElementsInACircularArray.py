from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxDist = 0
        for i in range(len(nums)):
            maxDist = max(maxDist, abs(nums[i]-nums[i-1]))
        return maxDist
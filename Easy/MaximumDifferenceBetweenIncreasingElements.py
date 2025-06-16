from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        mini = nums[0]
        maxi = nums[0]
        currentMax = -1
        for i in range(1,n):
            if nums[i] < mini:
                mini = nums[i]
                maxi = mini
            if nums[i]>maxi:
                maxi = nums[i]
                currentMax = max(currentMax, maxi-mini)

        return currentMax
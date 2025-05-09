from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        maxSum = minSum = nums[0]
        curMax = curMin = 0

        for num in nums:
            curMax = max (curMax +num, num)
            maxSum = max (maxSum, curMax)
            curMin = min (curMin + num, num)
            minSum = min (curMin, minSum)
            total += num

        return max(maxSum, total - minSum) if maxSum > 0  else maxSum
    
print(Solution().maxSubarraySumCircular([5,-3,5]))
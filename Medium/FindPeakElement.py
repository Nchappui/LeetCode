from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
    
# Test cases
solution = Solution()
print(solution.findPeakElement([1, 2, 3, 1]))  # Output: 2
print(solution.findPeakElement([1, 2, 1, 3, 5, 6]))  # Output: 5
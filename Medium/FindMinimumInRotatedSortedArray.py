from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Check if the middle element is greater than the last element
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
# Test cases
solution = Solution()
print(solution.findMin([3, 4, 5, 1, 2]))  # Output: 1
print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))  # Output: 0
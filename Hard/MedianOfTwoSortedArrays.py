from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        if len(merged) % 2 == 1:
            return float(merged[len(merged) // 2])
        else:
            return (merged[len(merged) // 2 - 1] + merged[len(merged) // 2]) / 2
# Test cases
solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
print(solution.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
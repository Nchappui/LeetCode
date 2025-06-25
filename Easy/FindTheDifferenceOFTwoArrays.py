from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(elem for elem in nums1 if elem not in nums2)),list(set(elem for elem in nums2 if elem not in nums1))]
    
    ##M MORE ELEGANT SOLUTION
    """
    class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
    """
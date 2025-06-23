import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = res = 0
        h = []
        for a,b in sorted(list(zip(nums1, nums2)), key=lambda ab: -ab[1]):
            heapq.heappush(h, a)
            total += a
            if len(h) > k:
                total -= heapq.heappop(h)
            if len(h) == k:
                res = max(res, total * b)
        return res
    
print(Solution().maxScore([1,3,3,2],[2,1,3,4],3))
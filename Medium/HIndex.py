from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        hIndex=0
        n = len(citations)
        
        for i in range(1, n + 1):
            if citations[n-i]>=i:
                hIndex = i
        return hIndex
    
print(Solution().hIndex([3,0,6,1,5])) ## 3
print(Solution().hIndex([0,0,2])) ## 1
print(Solution().hIndex([4])) ## 1
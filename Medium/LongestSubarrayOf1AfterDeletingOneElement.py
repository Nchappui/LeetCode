from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        currentLeft = 0
        currentRight = 0
        hasAZero = False
        for i in range(len(nums)):
            if nums[i]:
                currentRight += 1
            else:
                hasAZero = True
                if not currentLeft and currentRight:
                    currentLeft = currentRight
                    currentRight = 0
                elif currentLeft and currentRight:
                    res = max(res, currentLeft + currentRight)
                    currentLeft = currentRight
                    currentRight = 0
                elif currentLeft and not currentRight:
                    res = max(res, currentLeft)
                    currentLeft = currentRight = 0
        if currentLeft and currentRight:
            res = max(res, currentLeft + currentRight)
        elif not currentLeft and currentRight:
            res = max(res, currentRight if hasAZero else currentRight -1)
        elif currentLeft and not currentRight:
            res = max(res, currentLeft)
        
        return res
    
Solution().longestSubarray([1,1,0,1])
Solution().longestSubarray([0,1,1,1,0,1,1,0,1])
Solution().longestSubarray([1,1,1])
print(Solution().longestSubarray([0,0,0]))
print(Solution().longestSubarray([1,0,0]))
print(Solution().longestSubarray([0,1,1,0]))
print(Solution().longestSubarray([0,1,1]))
print(Solution().longestSubarray([1,0,1]))
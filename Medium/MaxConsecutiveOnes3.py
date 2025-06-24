from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = size = 0
        remainingZeroes = k
        n = len(nums)
        res = 0
        while right < n:
            if nums[right]:
                size += 1
                right += 1
            else:
                if remainingZeroes:
                    right += 1
                    size += 1
                    remainingZeroes -= 1
                else:
                    while nums[left]:
                        left+=1
                        size-=1
                    left += 1
                    right += 1
            res = max(res, size)
        return res
        
Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)
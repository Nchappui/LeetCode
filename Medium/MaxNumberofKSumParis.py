from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        res = 0
        while left < right:
            l = nums[left]
            r = nums[right]
            if l + r == k:
                res += 1
                left += 1
                right -=1
            elif l + r > k:
                right -=1
            else:
                left += 1
        
        return res
    
Solution().maxOperations([1,2,3,4],5)
            
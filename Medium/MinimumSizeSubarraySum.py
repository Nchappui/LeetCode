from typing import List


class Solution:

    ##DOUBLE FOR LOOP NOT SCALING
    def minSubArrayLenBad(self, target: int, nums: List[int]) -> int:
        for i in range(1, len(nums)+1):
            for j in range (len(nums)-i+1):
                if sum(nums[j : j+i]) >= target:
                    return i
        return 0
    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 1
        currentRes = nums[0]
        currentBest = float('inf')
        if currentRes >= target and end-start < currentBest:
                currentBest = end-start
        while start != len(nums)-1:
            if end == len(nums) or currentRes >= target :
                currentRes-=nums[start]
                start+=1
            else:
                currentRes+=nums[end]
                end+=1
            
            if currentRes >= target and end-start < currentBest:
                currentBest = end-start

        return currentBest if currentBest != float('inf') else 0       # type: ignore

print(Solution().minSubArrayLen(7,[1,1,1,1,7]))
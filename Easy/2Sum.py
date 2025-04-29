from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i in range(len(nums)):
            if nums[i] in numsMap:
                numsMap[nums[i]].append(i)
            else: numsMap[nums[i]] = [i]
        nums.sort()
        start = 0 
        end = len(nums)-1
        while start<end:
            if nums[start]+nums[end]>target:
                end-=1
            elif nums[start]+nums[end]<target:
                start+=1
            else:
                if nums[start] == nums[end]: return  numsMap[nums[start]]
                else: return numsMap[nums[start]] + numsMap[nums[end]]

    
print(Solution().twoSum([3,2,4], 6))
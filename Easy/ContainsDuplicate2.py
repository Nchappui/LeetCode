from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsMap = {}
        for i in range(len(nums)):
            if nums[i] in numsMap:
                if i - numsMap[nums[i]] <= k : return True
                else: numsMap[nums[i]] = i
            else: numsMap[nums[i]] = i
        return False
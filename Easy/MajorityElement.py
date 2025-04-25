from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums.sort()
        counter=1
        maxCounter=1
        ans=0
        for i in range(1, len(nums)):
            if nums[i]!=nums[i-1]:
                counter=1
            else:
                counter+=1
                if counter>maxCounter:
                    maxCounter=counter
                    ans=nums[i]
        return ans
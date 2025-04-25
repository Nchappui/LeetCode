from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter=0
        for i in range(1, len(nums)):
            if nums[i]!=nums[counter]:
                counter+=1
                nums[counter]=nums[i]

        return counter+1


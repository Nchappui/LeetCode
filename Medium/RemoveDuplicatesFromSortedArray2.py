from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter=2
        for i in range(2, len(nums)):
            if nums[i]!=nums[counter-2]:    
                nums[counter]=nums[i]
                counter+=1
        return counter
    
print(Solution().removeDuplicates([1,1,1,2,2,3]))
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter=0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i]=-1
            else:
                counter+=1
        nums.sort(reverse=True)
        return counter
    
print(Solution().removeElement([3,2,2,3],3))
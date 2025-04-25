from typing import List


class Solution:
    ##Working but scales poorly
    def canJump2(self, nums: List[int]) -> bool:
        curr = nums[0]
        if curr >= len(nums)-1:
            return True
        if nums[0] == 0:
            return False
        else:
            for i in range(curr):
                if self.canJump(nums[i+1:]):
                    return True
        return False
    
    def canJump(self, nums: List[int]) -> bool:
        currentGoal = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if(i+nums[i])>=currentGoal:
                currentGoal=i
        return True if currentGoal==0 else False


nums = [3,2,1,0,4]
solution = Solution()
print(solution.canJump(nums)) 
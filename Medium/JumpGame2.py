from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        currentGoal = len(nums)-1
        counter=0
            
        def findBiggest(goal, nums):
            currentBest=goal
            for i in range(len(nums)-2,-1,-1):
                if(i+nums[i])>=goal and i < currentBest:
                    currentBest=i
            return currentBest
        
        while(currentGoal!=0):
            currentGoal = findBiggest(currentGoal, nums)
            counter +=1
        return counter
    

print(Solution().jump([2,3,1,1,4]))
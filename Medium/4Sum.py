from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answerSet = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                LI, RI = j+1, len(nums)-1
                while(LI<RI):
                    sum = nums[LI]+nums[RI]+nums[i]+nums[j]
                    if(target==sum):
                        answerSet.add((nums[i],nums[j],nums[LI],nums[RI]))
                        LI+=1
                    elif(target<sum):
                        RI-=1
                    else:
                        LI+=1

        answer =[]
        for elem in answerSet:
            answer.append(list(elem))
        return answer
    
print(Solution().fourSum([1,0,-1,0,-2,2],0))
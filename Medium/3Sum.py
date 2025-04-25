from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answerSet = set()
        for index in range(len(nums)):
            LI, RI = index+1, len(nums)-1
            while(LI<RI):
                #print(LI, RI)
                if(-nums[index]==nums[LI]+nums[RI]):
                    answerSet.add((nums[index],nums[LI],nums[RI]))
                    LI+=1
                elif(-nums[index]<nums[LI]+nums[RI]):
                    RI-=1
                else:
                    LI+=1
        answer =[]
        for elem in answerSet:
            answer.append(list(elem))
        return answer
    
print(Solution().threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
                
            

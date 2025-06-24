from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = middle = potential = 0
        fLeft = fMiddle = fPotential = False
        for i in range(len(nums)):
            if not fLeft:
                fLeft = True
                left = nums[i]
            elif fLeft and nums[i]<left and not fMiddle:
                left = nums[i]
            elif fLeft and nums[i] > left and not fMiddle:
                fMiddle = True
                middle = nums[i]
            elif fLeft and nums[i] < middle and nums[i] > left and fMiddle:
                middle = nums[i]
            elif fLeft and fMiddle and nums[i] < left and not fPotential:
                potential = nums[i]
                fPotential = True
            elif fLeft and fMiddle and fPotential and nums[i] < potential:
                potential = nums[i]
            elif fPotential and nums[i] < middle and nums[i] > potential:
                left = potential
                middle = nums[i]
                fPotential = False
            elif fLeft and fMiddle and nums[i] > middle:
                return True
            
        return False
    
print(Solution().increasingTriplet([20,100,10,12,5,13]))
print(Solution().increasingTriplet([2,1,5,0,-1,6]))
print(Solution().increasingTriplet([2,1,5,0,1,6]))
print(Solution().increasingTriplet([2,1,5,0,4,5]))
print(Solution().increasingTriplet([2,1,5,4,4,5]))

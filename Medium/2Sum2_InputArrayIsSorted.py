from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        lIndex, rIndex = 0, n-1
        while lIndex<rIndex:
            if numbers[lIndex]+numbers[rIndex]==target: return [lIndex+1,rIndex+1]
            elif numbers[lIndex]+numbers[rIndex]>target : rIndex-=1
            else: lIndex +=1
        return False


    ##NOT WORKING SOLUTION
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i1=1
        i2=2
        while(True):
            if(numbers[i1-1]+numbers[i2-1] == target):
                return [i1, i2]
            if i1==i2-1:
                i2+=1
            elif i2==n:
                i1+=1
            else:
                if numbers[i1]-numbers[i1-1]>=numbers[i2]-numbers[i2-1]:
                    i2+=1
                else:
                    i1+=1
            if i1==n-1 and i2==n and numbers[i1-1]+numbers[i2-1] != target:
                return False
            
    ##WORKS BUT SCALES HORRIBLY
    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if(numbers[i]+numbers[j] == target):
                    return [i+1, j+1]
        return False
    
        
print(Solution().twoSum([3,24,50,79,88,150,345], 200))
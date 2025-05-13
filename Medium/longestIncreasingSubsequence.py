from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dpArray= []
        ans = 1
        for num in nums:
            dpArray.append([num,0])
        dpArray[-1][1] = 1
        for i in range(n-2,-1,-1):
            currentMax = 1
            for j in range(i+1,n):
                if dpArray[i][0]>=dpArray[j][0] and dpArray[j][1] == 1:
                    break
                if dpArray[i][0]<dpArray[j][0]:
                    currentMax = max(currentMax, dpArray[j][1] +1)
                    ans = max(currentMax, ans)
            dpArray[i][1]=currentMax
        return ans
    
print(Solution().lengthOfLIS([0,1,0,3,2,3]))

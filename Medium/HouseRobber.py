from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
    
        dpArray = [0] * n
        dpArray[0] = nums[0]
        dpArray[1] = max(nums[0],nums[1])
        for i in range (2,n):
            dpArray[i] = max(nums[i]+dpArray[i-2], dpArray[i-1])

        return dpArray[-1]

Solution().rob([1,2,3,1])

'''
        ### WORKING RECURSION SOLUTION BUT TLE
        def robHelper(i, n):
            if i == n-1:
                return nums[i]
            elif i == n-2:
                return max(nums[i], nums[i+1])
            else:
                return max(nums[i]+robHelper(i+2,n), robHelper(i+1,n))
            
        return robHelper(0,n)
        '''
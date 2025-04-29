from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        if len(nums) == 0 : return ans
        prev = nums[0]
        ans = []
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if prev != nums[i-1]:
                    ans.append(str(prev) + "->"+ str(nums[i-1]))
                    prev=nums[i]
                else:
                    ans.append(str(nums[i-1]))
                    prev=nums[i]

        if nums[len(nums)-1] == prev:
            ans.append(str(prev))
        else:
            ans.append(str(prev) + "->"+ str(nums[len(nums)-1]))
        return ans
print(Solution().summaryRanges([0,2,3,4,6,8,9]))
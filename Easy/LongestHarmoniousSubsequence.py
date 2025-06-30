
class Solution:
    def findLHS(self, nums):
        nums.sort()
        left = 0
        maxLength = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 1:
                left += 1
            if nums[right] - nums[left] == 1:
                maxLength = max(maxLength, right - left + 1)
        return maxLength
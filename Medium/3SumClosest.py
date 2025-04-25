from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = float('inf')
        for i in range(len(nums)):
            j,k = i+1, len(nums)-1
            while (j<k):
                sum = nums[i] + nums[j] + nums[k]
                diff = target - sum
                answer = sum if abs(diff) < abs(answer-target) else answer       
                if diff == 0:
                    return target
                elif sum<target:
                    j+=1
                else:
                    k-=1
        return answer

print(Solution().threeSumClosest(nums = [0,0,0], target = 1))
print(Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1))
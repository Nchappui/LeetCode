from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def recFunc(curr):
            validNumbers = nums.copy()
            if len(curr) == len(nums):
                answer.append(curr.copy())
                return
            for num in curr:
                validNumbers.remove(num)
            for num in validNumbers:
                curr.append(num)
                recFunc(curr)
                curr.pop()
        recFunc([])
        return answer
    
print(Solution().permute([1,2,3]))
print(Solution().permute([0,1]))
print(Solution().permute([1]))

from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = set()
        n = len(nums)
        for i in range(n):
            if nums[i] == key:
                mini = 0 if i-k <0 else i - k
                maxi = n if i+k+1 > n else i + k+1
                print(range(mini,maxi))
                indices.update(range(mini,maxi))
        
        return list(indices)
    
print(Solution().findKDistantIndices([3,4,9,1,3,9],9,1))
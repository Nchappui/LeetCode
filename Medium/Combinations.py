from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []
        def recFunc(start, curr):
            if len(curr) == k:
                result.append(curr.copy())
                return
            for i in range(start, n + 1):  
                curr.append(i)
                recFunc(i + 1, curr) 
                curr.pop() 
        recFunc(1, [])
        return result
    
print(Solution().combine(4,2))
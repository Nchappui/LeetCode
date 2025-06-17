from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [0]
        res = [0] * n
        for i in range(1, n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                id = stack.pop()
                res[id] = i - id
            stack.append(i)
        return res
    
Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
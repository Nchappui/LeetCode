from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def createSolution(used, currSum, x):
            if (currSum == n and x == 0):
                temp = used.copy()
                temp.sort()
                if temp not in res:
                    res.append(temp)
                return
            if len(used) == 9 or x == 0:
                return
            for i in [item for item in [1,2,3,4,5,6,7,8,9] if item not in used]:
                if currSum + i <= n:
                    used.append(i)
                    createSolution(used, currSum+i, x-1)
                    used.pop()
        createSolution([], 0, k)
        return res
    
print(Solution().combinationSum3(3,7))
print(Solution().combinationSum3(3,9))
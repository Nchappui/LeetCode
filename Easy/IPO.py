from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        oldCapital = float('-inf')
        currentCapital = w
        h = []
        for i in range(len(profits)):
            heapq.heappush(h, (capital[i],profits[i]))
        h2 = []    
        while k > 0:
            if currentCapital > oldCapital:
                while h and h[0][0]<=currentCapital:
                    temp = heapq.heappop(h)[1]
                    heapq.heappush(h2, -temp)
            if not h2 :
                return currentCapital
            profit = - heapq.heappop(h2)
            oldCapital = currentCapital
            currentCapital += profit
            k = k-1

        return currentCapital

print(Solution().findMaximizedCapital(2,0,[1,2,3],[0,1,1]))
print(Solution().findMaximizedCapital(3,0,[1,2,3],[0,1,2]))
print(Solution().findMaximizedCapital(1,0,[1,2,3],[1,1,2]))
print(Solution().findMaximizedCapital(11,11,[1,2,3],[11,12,13]))
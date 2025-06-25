import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        remaining = n = len(costs)
        res = 0
        left = []
        right = []
        leftIndex = 0
        rightIndex = n-1
        if k >= n:
            return sum(costs)
        if remaining <= 2*candidates:
            costs.sort()
            for i in range(k):
                res+= costs[i]
            return res
        for _ in range(candidates):
            heapq.heappush(left, costs[leftIndex])
            leftIndex += 1
            heapq.heappush(right, costs[rightIndex])
            rightIndex -= 1
        while k > 0:
            if not left:
                res += heapq.heappop(right)
            elif not right:
                res += heapq.heappop(left)
            elif left[0] <= right[0]:
                if remaining > 2* candidates:
                    res += heapq.heapreplace(left, costs[leftIndex])
                    leftIndex += 1 
                else:
                    res += heapq.heappop(left)
            else:
                if remaining > 2* candidates:
                    res+= heapq.heapreplace(right, costs[rightIndex])
                    rightIndex -= 1
                else:
                    res += heapq.heappop(right)
            remaining -= 1
            k -= 1
        return res

Solution().totalCost([25,65,41,31,14,20,59,42,43,57,73,45,30,77,17,38,20,11,17,65,55,85,74,32,84],24,8)
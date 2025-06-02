from collections import deque
import heapq
from typing import List


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        available = []
        assigned = []
        count = 0
        k = 0

        for i in range(len(nums)):
            while assigned and assigned[0] < i:
                heapq.heappop(assigned)
            while k < len(queries) and queries[k][0] <= i:
                heapq.heappush(available, -queries[k][1])
                k += 1
            while len(assigned) < nums[i] and available and -available[0] >= i:
                heapq.heappush(assigned, -heapq.heappop(available))
                count += 1
            if len(assigned) < nums[i]:
                return -1
        return len(queries) - count
        '''
        for i in range(len(nums)):
            while(nums[i]>0):
                if(sorted_queries[0][0]>i):
                    return -1
                while sorted_queries and sorted_queries[0][0] == i:
                        heapq.heappush(available, (-sorted_queries[0][1],sorted_queries[0][0]))
                        sorted_queries.pop(0)
                
                
                elif(sorted_queries[0][0]==i):
                    for j in range(i,sorted_queries[0][1]+1):
                        nums[j]-=1
                    sorted_queries.pop(0)

                else:
                    if not available: 
                        return -1
                    for j in range(available[0][1],-available[0][0]+1):
                        nums[j]-=1
                    available.pop(0)
                    
                    j = 0
                    max = 0
                    bestj = 0
                    while j < len(sorted_queries) and sorted_queries[j][0]<=i:
                        dist = sorted_queries[j][1]
                        if dist > max:
                            max = dist
                            bestj = j
                        j += 1
                    if max < i:
                        return -1
                    for j in range(sorted_queries[bestj][0],sorted_queries[bestj][1]+1):
                        nums[j]-=1
                    sorted_queries.pop(bestj)
                   
                if not sorted_queries:
                    for elem in nums:
                        if elem > 0:
                            return -1

        return len(sorted_queries)
 '''

print(Solution().maxRemoval([1,3],[[0,1],[0,1]]))
print(Solution().maxRemoval([3,2],[[0,1],[0,1],[0,1]]))
print(Solution().maxRemoval([0,3],[[0,1],[0,0],[0,1],[0,1],[0,0]]))
print(Solution().maxRemoval([1,1,1,1],[[1,3],[0,2],[1,3],[1,2],[0,3],[0,3]]))
print(Solution().maxRemoval([1,2,3,4],[[0,3], [0,2], [1,2]]))
print(Solution().maxRemoval([2,0,2],[[0,2],[0,2],[1,1]]))
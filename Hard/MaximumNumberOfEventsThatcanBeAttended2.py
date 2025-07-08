from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort(key = lambda x : (x[1],x[0],x[2]))
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        def binarySearch(currStart) -> int:
            left = 0
            right = n -1
            res = - 1
            while left<=right:
                mid = (int)(left + (right - left)/2)
                if events[mid][1] < currStart:
                    res = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return res   
        
        for i in range(1, n + 1):
            event = events[i-1]
            prev = binarySearch(event[0])
            for j in range(1, k+1):
                dp[i][j] = max(dp[i-1][j], dp[prev+1][j-1] + event[2])
        return dp[n][k]
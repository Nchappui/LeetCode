from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[1],x[0]))
        lastEnd = -float('inf')
        res = 0
        for interval in intervals:
            if interval[0] < lastEnd:
                res += 1
            else:
                lastEnd = interval[1]
                
        return res
    
Solution().eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]])
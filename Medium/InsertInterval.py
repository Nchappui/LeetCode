from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []: return [newInterval]
        if newInterval == []: return intervals
        minI = 0
        foundMin = False
        foundMax = False
        ans = []
        for i in range(len(intervals)):
            if foundMin and foundMax:
                ans.append(intervals[i])
            if newInterval[0]<=intervals[i][1] and not foundMin:
                minI = min(newInterval[0],intervals[i][0])
                foundMin = True
            if foundMin and newInterval[1]<=intervals[i][1] and not foundMax:
                if newInterval[1]<intervals[i][0]:
                    ans.append([minI,newInterval[1]])
                    ans.append(intervals[i])
                else:
                    ans.append([minI,intervals[i][1]])
                foundMax = True
            if not foundMin:
                ans.append(intervals[i])

        if not foundMin:
            return ans + [newInterval]

        if foundMin and not foundMax:
            ans.append([minI, max(newInterval[1], intervals[len(intervals)-1][1])])
            foundMax = True
        return ans
    
print(Solution().insert([[1,5]], [6,7]))


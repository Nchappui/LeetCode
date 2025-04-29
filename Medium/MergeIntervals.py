from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ans =[]
        intervals.sort(key = lambda x: (x[0], x[1]))
        smallestNumInInterval = intervals[0][0]
        biggestNumInInterval = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]>=smallestNumInInterval and intervals[i][1]<=biggestNumInInterval:
                continue
            elif intervals[i][0]<=biggestNumInInterval:
                biggestNumInInterval = intervals[i][1]
            else:
                ans.append([smallestNumInInterval,biggestNumInInterval])
                smallestNumInInterval = intervals[i][0]
                biggestNumInInterval = intervals[i][1]
        ans.append([smallestNumInInterval,biggestNumInInterval])
        return ans


print(Solution().merge([[1,4],[2,3]])) ##[[1,4]]
print(Solution().merge([[1,4],[0,4]])) ##[[0,4]]
print(Solution().merge([[1,4],[1,5],[0,4],[0,5],[0,4],[-1,5]])) ##[[1,5]]
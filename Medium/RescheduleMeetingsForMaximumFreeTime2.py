from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = dict()
        n = len(startTime)
        left = 0
        for i in range(n):
            right = startTime[i]
            if left != right:
                if right-left in gaps:
                    gaps[right-left].append(left)
                else:
                    gaps[right-left] = [left]
            left = endTime[i]
        if endTime[-1] != eventTime:
            if eventTime-endTime[-1] in gaps:
                gaps[eventTime-endTime[-1]].append(endTime[-1])
            else:
                gaps[eventTime-endTime[-1]] = [endTime[-1]]
                
        
        res = 0
        left = 0
        for i in range(n):
            leftgap = startTime[i] - left
            if i < n-1:
                rightgap = startTime[i+1] - endTime[i]
            else:
                rightgap = eventTime - endTime[i]
            size = endTime[i] - startTime[i]
            res = max(res, leftgap+rightgap)
            
            if(leftgap + rightgap + size > res):
                for gapsize in gaps:
                    if gapsize >= size:
                        if (gaps[gapsize] == [startTime[i]-leftgap] or gaps[gapsize] == [endTime[i]] or gaps[gapsize] == [startTime[i]-leftgap, endTime[i]]):
                            continue
                        res = leftgap + rightgap + size
                        break
         
            left = endTime[i]
            
        return res
print(Solution().maxFreeTime(10,[0,3,7,9],[1,4,8,10]))
print(Solution().maxFreeTime(5,[1,3],[2,5]))
            
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : (x[0], x[1]))
        maxX = points[0][1]
        res = 1
        for i in range(1,len(points)):
            if(maxX>points[i][1]):
                maxX=points[i][1]
            if(maxX<points[i][0]):
                res+=1
                maxX = points[i][1]
        return res
    
print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])) ##2
print(Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])) ##4
print(Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])) ##2
print(Solution().findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]])) ##2

                    
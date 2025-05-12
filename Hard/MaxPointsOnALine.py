from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = {}
        biggestLine = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a = (points[j][1]-points[i][1])/(points[j][1]-points[i][1])
                b = points[i][1]-a*points[0]
                for k in range(i+2, len(points)):
                    lines[a,b].append(points[k])
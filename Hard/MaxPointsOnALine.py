from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = {}
        ans = 1
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                if points[j][0]-points[i][0] != 0:
                    a = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                    b = points[i][1]-a*points[i][0]
                else:
                    a = points[i][0]
                    b = "_"
                if (a,b) not in lines.keys():
                    lines[(a,b)] = set()
                    lines[(a,b)].add(tuple(points[i]))
                    lines[(a,b)].add(tuple(points[j]))
                    ans = max(ans, len(lines[(a,b)]))
                else:
                    if b=="_":
                        if points[j][0] == a:
                            lines[(a,b)].add(tuple(points[j]))                      
                    elif 0<= abs(a * points[j][0] + b - points[j][1]) < 0.0000000000001:
                        lines[(a,b)].add(tuple(points[j]))
                    ans = max(ans, len(lines[(a,b)]))

        return ans

print(Solution().maxPoints([[-184,-551],[-105,-467],[-90,-394],[-60,-248],[115,359],[138,429],[60,336],[150,774],[207,639],[-150,-686],[-135,-613],[92,289],[23,79],[135,701],[0,9],[-230,-691],[-115,-341],[-161,-481],[230,709],[-30,-102]]))
print(Solution().maxPoints([[1,0],[0,0]]))
print(Solution().maxPoints([[1,4],[0,0]]))
print(Solution().maxPoints([[1,1],[2,2],[3,3]]))
print(Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))


from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
            
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i]) -1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[-1])
    

print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(Solution().minimumTotal([[-10]]))
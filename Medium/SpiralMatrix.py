from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        minI = minJ = -1
        i = j = 0
        for k in range(n*m):
            res.append(matrix[i][j])
            if j<n and i==minI+1:
                j+=1
                if j==n:
                    j = n = n-1
            if  j==n and i<m:
                i+=1
                if i==m:
                    i = m = m-1
            if j >= minJ and i == m:
                j = j-1
                if j==minJ:
                    j = minJ = minJ+1
                    minI+=1
            if j == minJ and i >= minI:
                i = i-1
                if i==minI:
                    minJ +=1

        return res
    
print(Solution().spiralOrder([
    [1,2,3,4,6,7],
    [1,2,3,4,6,7],
    [1,2,3,4,6,7],
    [5,6,7,8,6,7],
    [9,10,11,12,6,7]]))
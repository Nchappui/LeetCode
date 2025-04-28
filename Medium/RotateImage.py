from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def getIterationCount(val):
            if val == 1:
                return 0
            if val == 2:
                return 1
            else: return val-1 + getIterationCount(val-2) 


        min, max =0, n    
        j = 0
        for i in range(getIterationCount(n)):
            if j<max-1:
                matrix[min][min+j],matrix[min+j][max-1],matrix[max-1][max-j-1],matrix[max-j-1][min]=matrix[max-j-1][min],matrix[min][min+j],matrix[min+j][max-1],matrix[max-1][max-j-1]
                j+=1
                if j + min == max - 1:
                    j=0
                    max-=1
                    min+=1
        

Solution().rotate([[2,29,20,26,16,28],
                   [12,27,9,25,13,21],
                   [32,33,32,2,28,14],
                   [13,14,32,27,22,26],
                   [33,1,20,7,21,7],
                   [4,24,1,6,32,34]])
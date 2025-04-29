from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def setRowToZero(i, rowSize):
            for j in range(rowSize):
                matrix[i][j]=0
            
        def setColumnsToZero(i, columns, oldColumns):
            for j in columns:
                matrix[i][j]=0
            if (oldColumns):
                for j in range(i):
                    for k in oldColumns:
                        matrix[j][k] = 0
            

        columnIndices = set()
        oldColumns = set()
        setRow = False
        i = 0
        rowSize = len(matrix[0])
        for row in matrix:
            while 0 in row:
                if row.index(0) not in columnIndices:
                    oldColumns.add(row.index(0))
                    columnIndices.add(row.index(0))
                row[row.index(0)] = 1
                setRow = True
            if(setRow):
                setRowToZero(i, rowSize)
                setRow = False
            if(columnIndices and not setRow):
                setColumnsToZero(i, columnIndices, oldColumns)
                oldColumns = set()
            i+=1

Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]])

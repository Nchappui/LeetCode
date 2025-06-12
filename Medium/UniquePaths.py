class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * n for _ in range(m)]
        matrix[0][0] = 1
        for x in range(m):
            for y in range(n):
                if x==0 and y == 0:
                    continue
                matrix[x][y] = (matrix[x-1][y] if x-1 >= 0 else 0) + (matrix[x][y-1] if y-1 >= 0 else 0)
        
        return matrix[-1][-1]
    
Solution().uniquePaths(3,7)
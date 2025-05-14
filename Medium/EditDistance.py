class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dpArray = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2) + 1)]
        for x in range(1, len(word1)+1):
            dpArray[0][x] = x
        for y in range(1, len(word2)+1):
            dpArray[y][0] = y

        for x in range(1, len(word2) + 1):
            for y in range(1, len(word1) + 1):
                left = dpArray[x][y-1] + 1
                up = dpArray[x-1][y] + 1
                diag = dpArray[x-1][y-1] + (1 if word2[x-1] != word1[y-1] else 0)
                dpArray[x][y] = min (diag, min(left,up))

        return dpArray[-1][-1]

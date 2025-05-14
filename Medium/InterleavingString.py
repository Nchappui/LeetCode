class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        dpArray = [[False for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        dpArray[0][0] = True
        for x in range(1, len(s1)+1):
            if dpArray[0][x-1] and s3[x-1] == s1[x-1]:
                dpArray[0][x] = True
        for y in range(1, len(s2)+1):
            if dpArray[y-1][0] and s3[y-1] == s2[y-1]:
                dpArray[y][0] = True


        for x in range(1, len(s2) + 1):
            for y in range(1, len(s1) + 1):
                if (dpArray[x-1][y] and s3[x+y-1] == s2[x-1]) or (dpArray[x][y-1] and s3[x+y-1] == s1[y-1]):
                    dpArray[x][y] = True
                else:
                    dpArray[x][y] = False

        return dpArray[-1][-1]



    #Working solution but TLE
    '''
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ans = False
        if len(s1)  + len(s2) != len(s3): return False
        def recFunc(current, s1, s2, s3):
            if current == s3:
                nonlocal ans
                ans = True
            else:
                if s1 and s1[0] == s3[len(current)]:
                    recFunc(current + s1[0], s1[1:], s2, s3)
                if s2 and s2[0] == s3[len(current)]:
                    recFunc(current + s2[0], s1, s2[1:], s3)
        recFunc("", s1, s2, s3)
        return ans
    '''
print(Solution().isInterleave("abc","def","adbecf"))
print(Solution().isInterleave("aabcc","dbbca","aadbbcbcac"))
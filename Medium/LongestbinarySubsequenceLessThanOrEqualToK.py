class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = 0
        curr = 0
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i] == '0':
                res += 1
            elif curr + pow(2,n-1-i) <= k:
                res += 1
                curr += pow(2,n-1-i)
        return res
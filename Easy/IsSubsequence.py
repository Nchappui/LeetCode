class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index=0
        if s=="": return True
        for i in range(len(t)):
            if(s[index]==t[i]):
                index+=1
            if index == len(s):
                return True
        return False
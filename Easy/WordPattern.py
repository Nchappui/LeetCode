class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapS = {}
        t = s.split(" ")

        if (len(pattern)!=len(t)): return False
        for i in range(len(pattern)) :
            if pattern[i] in mapS:
                if t[i] != mapS[pattern[i]]:
                    return False
            else:
                if t[i] in mapS.values(): return False
                mapS[pattern[i]] = t[i]
        return True
    
Solution().wordPattern("aaa", "aa aa aa aa")
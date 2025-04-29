class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS = {}

        for i in range(len(s)) :
            if s[i] in mapS:
                if t[i] != mapS[s[i]]:
                    return False
            else:
                if t[i] in mapS.values(): return False
                mapS[s[i]] = t[i]
        return True
        ## Didn't understand the problem correctly
        '''
        mapT = {}

        for char in s:
            mapS[char] = 1 + mapS.get(char, 0)
        for char in t:
            mapT[char] = 1 + mapT.get(char, 0)

        print(mapS)
        print(mapT)

        return sorted(list(mapS.values())) == sorted(list(mapT.values()))
        '''
print(Solution().isIsomorphic("badc", "baba"))
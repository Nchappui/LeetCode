class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        start, end = 0, 1
        ans = ""
        neededLetters = list(t)

        dictNeeded = {}
        for elem in neededLetters:
            if elem in dictNeeded:
                  dictNeeded[elem] += 1
            else:
                 dictNeeded[elem] = 1
             

        if n>m : return ""

        while t.find(s[start]) == -1:
            start += 1
            end += 1
            if (end>m):
                 return ""
            
        if (t.find(s[start]) != -1):
            neededLetters.remove(s[start])
            dictNeeded[s[start]] -=1

        currentWord = s[start:end]
        if neededLetters == []:
                if ans == "": ans = currentWord
                else:
                        if len(ans)>len(currentWord): ans = currentWord

        def isNeeded(start, dictNeeded):
            if s[start] not in t:
                return False
            else:
                if dictNeeded[s[start]] < 0 :
                    dictNeeded[s[start]]+=1
                    return False
                return True

        while end<m:
            currentLetter = s[end]
            currentWord+=s[end]
            ## Letter is already present at first position and not needed
            if currentLetter == s[start] and not (s[start]) in neededLetters:
                    start+=1
                    currentWord=currentWord[1:]
                    while not isNeeded(start, dictNeeded):
                         start +=1
                         currentWord=currentWord[1:]
            elif currentLetter in t :
                dictNeeded[currentLetter] -=1
                if currentLetter in neededLetters:
                    neededLetters.remove(currentLetter)
            if neededLetters == []:
                if ans == "": ans = currentWord
                else:
                        if len(ans)>len(currentWord): ans = currentWord
            end +=1


        return ans
    
print(Solution().minWindow("ADOBECODEBANC", "ABC")) ##BANC

print(Solution().minWindow("a", "a")) ##a

print(Solution().minWindow("a", "aa")) ##""

print(Solution().minWindow("ADOBECODEBANC", "BABC")) ##BECODEBANC

print(Solution().minWindow("ab", "b")) ##b
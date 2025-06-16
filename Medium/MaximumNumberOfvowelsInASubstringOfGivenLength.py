class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel (c):
            if c in "aeiou":
                return True
            else: return False

        count = 0
        maxCount = 0
        vowelArray = [False] * len(s)
        for i in range(k):
            temp = isVowel(s[i])
            vowelArray[i] = temp
            if temp:
                count+=1


        maxCount = max(count, maxCount)
        if count == k: return k

        start = vowelArray[0]
        for i in range(k, len(s)):
            if start: count -= 1
            start = vowelArray[i-k+1]
            vowelArray[i] = isVowel(s[i])
            if vowelArray[i]: 
                count += 1
                maxCount = max(count, maxCount)
                if count == k: return k
            
        return maxCount
    
Solution().maxVowels("rhythms",1)
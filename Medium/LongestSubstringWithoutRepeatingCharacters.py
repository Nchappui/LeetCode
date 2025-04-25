class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s : return 0
        start, end = 0, 1
        currentRes = 1 
        currentSubstring = s[0]
        currentBest = 1 
        while start < len(s)-1:
            if end == len(s) or s[end] in currentSubstring :
                currentRes-=1
                currentSubstring = currentSubstring[1:]
                start+=1
            else:
                currentRes+=1
                currentSubstring += s[end]
                end+=1
                currentBest = max (currentBest, len(currentSubstring))


        return max (currentBest, currentRes)
    
print(Solution().lengthOfLongestSubstring(""))
print(Solution().lengthOfLongestSubstring(" "))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("dvdf"))
print(Solution().lengthOfLongestSubstring("au"))
print(Solution().lengthOfLongestSubstring("aud"))
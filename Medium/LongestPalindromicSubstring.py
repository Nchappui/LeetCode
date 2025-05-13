class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 1
        str = s[0]
        for i in range(len(s)):
            start = i-1
            end = i+1
            temp = 1
            while start >= 0 and end <= len(s)-1 and s[start] == s[end]:
                temp +=2
                if temp > ans:
                    ans = temp
                    str = s[start:end+1]
                start -=1
                end += 1


            start = i
            end = i+1
            temp = 0
            while start >= 0 and end <= len(s)-1 and s[start] == s[end]:
                temp +=2
                if temp > ans:
                    ans = temp
                    str = s[start:end+1]
                start -=1
                end += 1


        return str
    
print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
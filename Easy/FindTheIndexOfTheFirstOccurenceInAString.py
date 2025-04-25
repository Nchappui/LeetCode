class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range (len(haystack)-len(needle)+1):
            if(haystack[i:i+len(needle)]==needle):
                return i
        return -1
# Test cases    

print(Solution().strStr("sadbutsad", "sad"))  # Output: 2
print(Solution().strStr("a", "a"))  # Output: -1
print(Solution().strStr("abc", "c"))
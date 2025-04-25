class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitisedString = ""
        for i in range(len(s)):
            if s[i].isalnum():
                sanitisedString+=s[i].lower()
        return sanitisedString == sanitisedString[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))
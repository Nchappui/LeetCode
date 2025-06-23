class Solution:
    def reverseVowels(self, s: str) -> str:
        sList = list(s)
        left = 0
        right = len(s)-1
        vowels = "aeiouAEIOU"
        while right > left:
            while right != left and s[left] not in vowels:
                left += 1
            while right != left and s[right] not in vowels:
                right -= 1
            if right != left:
                sList[left], sList[right] = sList[right], sList[left]
                left += 1
                right -= 1
        return "".join(sList)
    
print(Solution().reverseVowels("AaU"))
print(Solution().reverseVowels("Aa"))
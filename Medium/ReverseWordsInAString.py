class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        isWord=False
        tempWord=""
        
        for i in range(len(s)):
            if(s[i] != ' '):
                isWord = True
                tempWord +=s[i]

            if(isWord and s[i] == ' '):
                isWord = False
                if result : result = tempWord + " "+result
                else : result = tempWord
                tempWord = ""
        if not result : return tempWord

        if tempWord and result : result = tempWord + " "+result

        return result

    ##BETTER SOLUTION  
    def reverseWords2(self, s: str) -> str:
        words = s.split()
        left, right = 0, len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        
        print(words)

        return " ".join(words) 
    
print(Solution().reverseWords2("the sky is blue"))
print(Solution().reverseWords2("  hello world  "))
print(Solution().reverseWords2("a good   example"))
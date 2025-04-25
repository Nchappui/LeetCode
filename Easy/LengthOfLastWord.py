class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1]
        beginCount=False
        res=0
        for i in range(len(s)):
            if res==0 and s[i] != ' ':
                res+=1
            elif res>0 and s[i] != ' ':
                res+=1
            
            if res>0 and s[i] == ' ':
                break
        return res
    
print(Solution().lengthOfLastWord("   fly me   to   the moon  "))

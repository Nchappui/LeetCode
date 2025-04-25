class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        while(s!=''):
            if (len(s)>1 and romanDict[s[0:1]]<romanDict[s[1:2]]):
                result -= romanDict[s[0:1]]
                result += romanDict[s[1:2]]
                s = s[2::]
            else:
                result += romanDict[s[0:1]]
                s = s[1::]

        return result
    
print(Solution().romanToInt('MCMXCIV')) 
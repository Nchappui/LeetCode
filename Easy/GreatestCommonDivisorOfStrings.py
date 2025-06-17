import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        maxLen = math.gcd(len(str1),len(str2))
        i = 0
        res = ""
        while len(res)<maxLen and str1[i]==str2[i]:
            res += str1[i]
            i += 1
        validated = False
        while res and not validated:
            n = len(res)
            if len(str1)/n == len(str1)//n and len(str2)/n == len(str2)//n:
                validated = True
                for i in range(len(str1)//n):
                   if str1[i*n:(i+1)*n] != res:
                       validated = False
                       break
               
                for i in range(len(str2)//n):
                    if str2[i*n:(i+1)*n] != res:
                        validated = False
                        break
                if validated:
                    return res

            res = res[:-1]
            
        return res

    
print(Solution().gcdOfStrings("AAAAAA","AAB"))
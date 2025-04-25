from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recFunc(curr, oC, cC, n):
            if(oC == cC and oC == n):
                res.append(curr)
                return
            if(oC<n):
                recFunc(curr+"(", oC+1, cC, n)
            if(cC<oC):
                recFunc(curr+")", oC, cC+1, n)
        recFunc("(",1,0,n)
        return res
    
print(Solution().generateParenthesis(3))
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevValue = prices[0]
        res=0
        for newprice in prices[1:]:
            if prevValue < newprice:
                res+=(newprice-prevValue)
            prevValue=newprice
        return res
    
print(Solution().maxProfit([5,3,10,1,4,6]))
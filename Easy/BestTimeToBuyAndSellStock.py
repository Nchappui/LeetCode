from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for elem in prices[1:]:
            if elem<buy:
                buy = elem
            
            profit = max (profit, elem - buy)

        return profit
    
print(Solution().maxProfit([7,6,5,3,10,1,4,6]))
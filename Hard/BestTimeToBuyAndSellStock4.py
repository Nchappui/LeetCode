from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        profitAfterBuy = [-1001 for _ in range (k+1)]
        profitAfterSell = [0 for _ in range (k+1)]

        for i in range(n):
            currentPrice = prices[i]
            for j in range(k,0,-1):
                profitAfterBuy[j] = max(profitAfterBuy[j],profitAfterSell[j-1]-currentPrice)
                profitAfterSell[j] = max(profitAfterSell[j], profitAfterBuy[j] + currentPrice)
        
        return profitAfterSell[k]
    

print(Solution().maxProfit(2,[3,3,5,0,0,3,-1,4]))
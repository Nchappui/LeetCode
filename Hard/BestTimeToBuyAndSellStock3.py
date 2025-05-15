from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = [0 for _ in range(n)]
        maxProfit = prices[n-1]
        for i in range(n-2, -1, -1):
            maxProfit = max(maxProfit, prices[i])
            profit[i] = max(maxProfit - prices[i], profit[i+1]) #in case prices[i] is negative

        minPrice = prices[0]
        for i in range(1, n):
            minPrice = min(minPrice, prices[i])
            profit[i] = max(profit[i-1], profit[i] + (prices[i]-minPrice))
        
        return profit[n-1]
    
print(Solution().maxProfit([3,3,5,0,0,3,-1,4]))
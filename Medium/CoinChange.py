import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse= True)
        dpArray=[0] + [-1]*amount
        gcd = math.gcd(*coins)
        for i in range(gcd, amount+1, gcd):
            for x in coins:
                start = i - x
                if start >= 0 and dpArray[start]>=0:
                    if dpArray[i] == -1:
                        dpArray[i] = dpArray[start]+1
                    else:
                        dpArray[i]=min(dpArray[i],dpArray[start]+1)
                    

        return dpArray[-1]
    

print(Solution().coinChange([2], 4))
print(Solution().coinChange([1, 2147483647], 2))
print(Solution().coinChange([2147483647], 2))
print(Solution().coinChange([186,419,83,408], 6249))
print(Solution().coinChange([1,6,7,10], 13))

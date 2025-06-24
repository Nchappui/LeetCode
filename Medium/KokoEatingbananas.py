import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        diff = h-n
        if diff < n-1 :
            piles.sort(reverse = True)
            if h <= n:
                return piles[0]
            return max(math.ceil(piles[(diff-1)%n]/(((diff-1)//n)+2)),math.ceil(piles[diff%n]/((diff//n)+1)))
        else:
            def hours_needed(speed):
                return sum((pile + speed - 1) // speed for pile in piles)

            left, right = 1, max(piles)

            while left < right:
                mid = (left + right) // 2
                if hours_needed(mid) <= h:
                    right = mid
                else:
                    left = mid + 1

            return left   
Solution().minEatingSpeed([3,6,7,11],8)
Solution().minEatingSpeed([30,11,23,4,20],5)
Solution().minEatingSpeed([30,11,23,4,20],6)
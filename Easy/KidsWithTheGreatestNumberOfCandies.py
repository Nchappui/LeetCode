from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        maxKid = max(candies)
        for i in range(n):
            if candies[i] + extraCandies >= maxKid:
                candies[i] = True
            else:
                candies[i]=False
        return candies # type: ignore
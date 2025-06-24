from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        curr = 0
        for i in range(len(gain)):
            curr += gain[i]
            res = max(res, curr)
        return res
        
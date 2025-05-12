from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curr = 0
        ans = []
        for num in digits:
            curr *=10
            curr += num
        curr += 1
        while curr > 0:
            ans.insert(0,curr%10)
            curr //= 10
        return ans
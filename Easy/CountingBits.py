from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(n+1):
            temp = bin(i)
            count = 0
            for c in temp:
                if c == '1':
                    count += 1
            res[i] = count
        return res
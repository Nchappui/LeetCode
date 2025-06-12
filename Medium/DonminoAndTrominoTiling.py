class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 5
        array = [0] * (n+1)
        array[0] = 0
        array[1] = 1
        array[2] = 2
        array[3] = 5
        for i in range(4, n+1):
            array[i] = 2*array[i-1]+array[i-3]
        return array[-1]%(1000000007)
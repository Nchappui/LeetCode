from collections import defaultdict
class Solution:
    def maxDifference(self, s: str) -> int:
        frequencies = defaultdict(int)
        for char in s:
            frequencies[char] += 1

        minEven = 101
        maxOdd = 0
        for key, value in frequencies.items():
            ## even
            if not value%2:
                minEven = min(minEven, value)
            ## odd
            else:
                maxOdd = max(maxOdd, value)
        return maxOdd-minEven

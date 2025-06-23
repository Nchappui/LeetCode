from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = defaultdict(int)
        for elem in arr:
            occurences[elem] += 1
            
        return len(occurences.values()) == len(set(occurences.values()))
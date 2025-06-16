import math
from typing import List
from collections import defaultdict


class Solution:
    def successfulPairs(self, spells, potions, success):
        n = len(spells)
        m = len(potions)
        pairs = [0] * n
        potions.sort()
        for i in range(n):
            spell = spells[i]
            left = 0
            right = m - 1
            while left <= right:
                mid = left + (right - left) // 2
                product = spell * potions[mid]
                if product >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            pairs[i] = m - left
        return pairs


        ###WORKING BUT TLE
        """
        n = len(spells)
        m = len(potions)
        potionsDict = defaultdict(int)
        potions.sort()

        potionKeys = []
        for i in range(m):
            potionsDict[potions[i]] = i +1
        for elem in potionsDict.keys():
            potionKeys.append(elem)

        for i in range(n):
            minPotVal = math.ceil(success / spells[i])
            if minPotVal in potionKeys:
                unFit = potionKeys.index(minPotVal) - 1
                spells[i] = m - potionsDict[potionKeys[unFit]] if unFit != -1 else m
            else:
                potionKeys.append(minPotVal)
                potionKeys.sort()
                unFit = potionKeys.index(minPotVal) - 1
                spells[i] = m - potionsDict[potionKeys[unFit]] if unFit != -1 else m
                potionKeys.remove(minPotVal)

        return(spells)
    """

Solution().successfulPairs([36,36,22,11,35,21,4,25,30,35,31,10,8,39,7,22,18,9,23,30,9,37,22,7,36,40,17,37,38,27,6,15,1,15,7,31,36,29,9,15,3,37,15,17,25,35,9,21,5,17,25,8,18,25,7,19,4,33,9,5,29,13,9,18,5,10,31,6,7,24,13,11,8,19,2],
                           [30,11,5,20,19,36,39,24,20,37,33,22,32,28,36,24,40,27,36,37,38,23,39,11,40,19,37,32,25,29,28,37,31,36,32,40,38,22,17,38,20,33,29,17,36,33,35,25,28,18,17,19,40,27,40,28,40,40,40,39,17,34,36,11,22,29,22,35,35,22,18,34],
                           135)
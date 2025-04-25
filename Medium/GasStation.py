from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalCost = totalGas = 0
        n = len(gas)
        currentgas = 0
        currentbest = 0
        for i in range(n):
            totalCost += cost[i]
            totalGas += gas[i]
            currentgas += gas[i] - cost[i]
            if currentgas<0:
                currentgas=0
                currentbest=i+1
        if totalCost>totalGas: return -1
        else: return currentbest
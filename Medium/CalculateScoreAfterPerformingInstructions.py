from typing import List


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        currentIndex = 0
        visitedIndices = set()
        score = 0
        while currentIndex >= 0 and currentIndex < n and currentIndex not in visitedIndices :
            visitedIndices.add(currentIndex)
            if instructions[currentIndex] == "jump":
                currentIndex += values[currentIndex]
            else:
                score += values[currentIndex]
                currentIndex += 1
        
        return score
    
print(Solution().calculateScore(["jump","add","add","jump","add","jump"],[2,1,3,1,-2,-3]))
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for elem in asteroids:
            if stack and stack[-1] > 0 and elem < 0:
                while stack and stack[-1] > 0 and elem:
                    if abs(elem) > stack[-1]:
                        stack.pop()
                    elif abs(elem) == stack[-1]:
                        stack.pop()
                        elem = 0
                    else:
                        elem = 0
                if elem:
                    stack.append(elem)
            else:
                stack.append(elem)
                
        return stack
from collections import defaultdict, deque
from typing import List


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        numDependencies = [0] * numCourses

        for course, prereq in prerequisites:
            graph.setdefault(prereq, []).append(course)
            numDependencies[course] += 1

        canBeDone = []
        for i in range(numCourses):
            if numDependencies[i] == 0:
                canBeDone.append(i)
        result = []

        while canBeDone:
            current = canBeDone.pop(0)
            result.append(current)

            for neighbor in graph[current]:
                numDependencies[neighbor] -= 1
                if numDependencies[neighbor] == 0:
                    canBeDone.append(neighbor)

        return result if len(result) == numCourses else []

print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
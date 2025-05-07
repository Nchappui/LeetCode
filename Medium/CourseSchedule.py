from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Construire le graphe
        graph = []
        for _ in range(numCourses):
            graph.append([])
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # Marquages pour les nœuds
        visited = set()  # Nœuds visités dans le chemin actuel (pour détecter les cycles)
        tested = set()   # Nœuds déjà vérifiés (sans cycle)

        def checkCycle(course):
            if course in visited:  # Cycle détecté
                return True
            if course in tested:   # Ce nœud a déjà été vérifié
                return False

            # Ajouter le cours au chemin actuel
            visited.add(course)
            for prereq in graph[course]:
                if checkCycle(prereq):  # Vérifier les dépendances
                    return True
            # Retirer le cours du chemin actuel et marquer comme testé
            visited.remove(course)
            tested.add(course)
            return False

        # Vérifier chaque cours
        for course in range(numCourses):
            if checkCycle(course):
                return False

        return True
    
Solution().canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]])
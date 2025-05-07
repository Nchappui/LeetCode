from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        graph = {}
        
        def tryMutation(gene):
            for i in range(len(gene)):
                otherLetters = ['A', 'C', 'G', 'T']
                otherLetters.remove(gene[i])
                for x in otherLetters:
                    newGene = gene[0:i] + x + gene[i+1 : len(gene)]
                    if newGene in bank:
                        graph.setdefault(gene, []).append(newGene)
        
        tryMutation(startGene)
        for gene in bank:
            tryMutation(gene)

        queue = [(startGene, 0)]
        seen = set()

        while (queue):
            curr, count = queue.pop(0)

            if curr == endGene :
                return count
            
            if curr in seen:
                continue

            seen.add(curr)
            if curr in graph:
                for nextGene in graph[curr]:
                    queue.append((nextGene, count+1))

        return -1

        
print(Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))

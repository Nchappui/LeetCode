from collections import defaultdict
from typing import List
from string import ascii_lowercase


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        generic_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                generic_word = word[:i] + "*" + word[i+1:]
                generic_dict[generic_word].append(word)

        queue = [(beginWord, 1)]
        seen = set()

        while (queue):
            curr, count = queue.pop(0)

            if curr == endWord :
                return count
            
            for i in range(len(curr)):
                generic_word = curr[:i] + "*" + curr[i+1:]
                for neighbor in generic_dict[generic_word]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, count + 1))

                # Une fois exploré, on peut vider la liste pour éviter des vérifications inutiles
                generic_dict[generic_word] = []

        return 0
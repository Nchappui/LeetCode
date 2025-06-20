from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        
        for i in range(len(word1)):
            dict1[word1[i]] += 1
            dict2[word2[i]] += 1
            
        val1 = list(dict1.values())
        val2 = list(dict2.values())
        val1.sort()
        val2.sort()
        key1 = set(dict1.keys())
        key2 = set(dict2.keys())
        if val1 == val2 and key1 == key2:
            return True
        return False
    
Solution().closeStrings("cabbba", "aabbss")
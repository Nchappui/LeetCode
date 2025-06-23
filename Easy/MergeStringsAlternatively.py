class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for _ in range(min(len(word1),len(word2))):
            res += word1[0]
            word1 = word1[1:]
            res += word2[0]
            word2 = word2[1:]
        res += word1
        res += word2
        return res        
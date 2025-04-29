class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        neededLetters = {}
        for elem in ransomNote :
            neededLetters[elem] = 1 + neededLetters.get(elem, 0)

        for c in magazine:
            if c in neededLetters:
                neededLetters[c] -=1
        
        for key in neededLetters:
            if neededLetters[key] > 0 : return False

        return True
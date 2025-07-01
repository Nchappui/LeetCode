
class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = word[0]
        count = 0
        for letter in word[1:]:
            if letter == prev:
                count += 1
            else:
                prev = letter
        return count + 1
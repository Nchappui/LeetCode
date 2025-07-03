class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ["a"]
        while len(word)<k:
            for letter in word.copy():
                if letter == "z":
                    word.append("a")
                else:
                    word.append(chr(ord(letter)+1))
        return word[k-1]
                
Solution().kthCharacter(5)
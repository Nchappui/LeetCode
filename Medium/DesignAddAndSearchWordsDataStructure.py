class WordDictionary:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        curr = self.tree
        for letter in word:
            if letter not in curr.keys():
                curr[letter] = {}
            curr = curr[letter]
        curr["*"] = {}
        

    def search(self, word: str) -> bool:
        curr = self.tree
        result = False
        def searchInTree(word, tree):
            if word == "":
                if "*" in tree.keys():
                    nonlocal result
                    result = True
                return
            letter = word[0]
            word = word[1:]
            if letter == ".":
                for key in tree.keys():
                    searchInTree(word, tree[key])
            elif letter in tree.keys():
                searchInTree(word, tree[letter])
                
        searchInTree(word, curr)
        return result


wordDictionary = WordDictionary()
wordDictionary.addWord("a")
wordDictionary.addWord("ab")
print(wordDictionary.search("a"))# return True
print(wordDictionary.search("a."))# return True
print(wordDictionary.search("ab")) # return True
print(wordDictionary.search(".a")) # return False
print(wordDictionary.search(".b")) # return True
print(wordDictionary.search("ab.")) # return False
print(wordDictionary.search(".")) # return True
print(wordDictionary.search("..")) # return True
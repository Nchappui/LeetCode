from typing import List

class TrieNode:
    def __init__(self) -> None:
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]

    def returnElems(self):
        result = []
        def dfs(node, path):
            if path:  # On évite d'ajouter la racine vide
                result.append(int(path))
            for digit in node.children:
                dfs(node.children[digit], path + digit)
        dfs(self.root, "")
        return result
                

class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        trie = Trie()
        for i in range(1, n+1):
            trie.insert(str(i))
        return trie.returnElems()
    
print(Solution().lexicalOrder(10))
        

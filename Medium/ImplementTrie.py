class TreeNode:
    def __init__(self, val="", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self):
        self.tree = TreeNode("_")

    def insert(self, word: str) -> None:
        if self.tree.val == "_":
            self.tree.right = TreeNode(word)
            self.tree = self.tree.right
        else:
            curr = self.tree
            while curr:
                prev = curr
                if word > curr.val:
                    curr=curr.right
                else:
                    curr=curr.left
            if word > prev.val:
                prev.right = TreeNode(word)
            else:
                prev.left = TreeNode(word)

        

    def search(self, word: str) -> bool:
        curr = self.tree
        if curr.val == word:
            return True
        else:
            while curr:
                if word > curr.val:
                    curr=curr.right
                else:
                    curr=curr.left
                if curr:
                    if curr.val == word:
                        return True
            return False
        

    def startsWith(self, prefix: str) -> bool:
        l = len(prefix)
        curr = self.tree
        if curr.val[:l] == prefix:
            return True
        else:
            while curr:
                if prefix > curr.val[:l]:
                    curr=curr.right
                else:
                    curr=curr.left
                if curr:
                    if curr.val[:l] == prefix:
                        return True
            return False
        

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionnaire pour les enfants
        self.is_end = False  # Indique si c'est la fin d'un mot


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.is_end = True  # Marquer la fin du mot

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.is_end  # Vérifie si c'est la fin d'un mot

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True  # Si on peut parcourir tout le préfixe, il existe

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))
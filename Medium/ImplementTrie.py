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
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))
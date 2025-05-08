from typing import List

### TRIE BASED ON THE LETTERS GRID, NOT WORKING NO IDEA WHY
class SolutionFalse:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = {}

        def contructTries(taken: List[tuple], x, y, currentTree):
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x,y) not in taken:
                if board[x][y] not in currentTree.keys():
                    currentTree[board[x][y]] = {}
                taken.append((x,y))
                takenCopy=taken.copy()
                temp = currentTree[board[x][y]]
                contructTries(takenCopy, x+1, y, temp)
                contructTries(takenCopy, x-1, y, temp)
                contructTries(takenCopy, x, y+1, temp)
                contructTries(takenCopy, x, y-1, temp)
                

        def searchWord(word, currentTree):
            for letter in word:
                if letter not in currentTree.keys():
                    return False
                currentTree = currentTree[letter]
            return True
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                taken = list()
                contructTries(taken, x, y, tree)

        res = []
        for word in words:
            tempTree = tree
            if searchWord(word, tempTree):
                res.append(word)
            
        return res
    


print(Solution().findWords([["c","d"],
                            ["b","a"]],
                            ["abc","abcd"]))

print(Solution().findWords([["a","b","c","e"],
                            ["x","x","c","d"],
                            ["x","x","b","a"]],
                            ["abc","abcd"]))

print(Solution().findWords([["a","b"]],
                            ["ba"]))

print(Solution().findWords([["a","a"]],
                            ["a"]))

print(Solution().findWords([["o","a","a","n"],
                            ["e","t","a","e"],
                            ["i","h","k","r"],
                            ["i","f","l","v"]],
                            ["oath","pea","eat","rain"]))
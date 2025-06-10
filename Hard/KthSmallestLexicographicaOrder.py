"""
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

    def returnIthElem(self, num) -> int:
        def dfs(node, path):
            nonlocal num
            if path:  # On évite d'ajouter la racine vide
                if num == 1:
                    return(int(path))
                num -= 1
            for digit in node.children:
                res = dfs(node.children[digit], path + digit)
                if res:
                    return res
            return None
        return dfs(self.root, "")  # type: ignore
"""
class Solution(object):
    def findKthNumber(self, n, k):
        return self.solve(0, n, k)

    def solve(self, current, n, k):
        if k == 0:
            return current // 10

        for i in range(max(current, 1), current + 10):
            count = self.numOfChildren(i, i + 1, n)
            if count >= k:
                return self.solve(i * 10, n, k - 1)
            k -= count

        return -1  

    def numOfChildren(self, current, neighbour, n):
        if neighbour > n:
            if current > n:
                return 0
            return n - current + 1
        return (neighbour - current) + self.numOfChildren(current * 10, neighbour * 10, n)



###TRES COOL MAIS TLE
"""
class Solution:
    class newComp:
        def __init__(self, val : int):
            self.val = val

        def __lt__(self, other):
            strVal = str(self.val)
            strOther = str(other.val)
            minVal = min(len(strVal), len(strOther))
            for i in range(minVal):
                if int(strVal[i]) < int(strOther[i]):
                    return True
                elif int(strVal[i]) > int(strOther[i]):
                    return False
            if minVal == len(strVal):
                return True
            return False
        

    def findKthNumber(self, n: int, k: int) -> int:
        h = []
        for i in range(1, n+1):
            h.append(Solution().newComp(i))
        
        h.sort()
        return h[i-1]

        for elem in h:
            print(elem.val)
        return h[k-1].val
        for _ in range(k-1):
            heapq.heappop(h)
        return heapq.heappop(h).val
"""
    
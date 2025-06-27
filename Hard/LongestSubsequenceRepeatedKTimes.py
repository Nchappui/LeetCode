from collections import defaultdict, deque
import math


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isK(sub: str, t: str, k: int) -> bool:
            count = i = 0
            for ch in t:
                if i < len(sub) and ch == sub[i]:
                    i += 1
                    if i == len(sub):
                        i = 0
                        count += 1
                        if count == k:
                            return True
            return False
        
        letters = defaultdict(int)
        for letter in s:
            letters[letter] += 1
        if max(letters.values()) < k:
            return ""
        
        else:
            possibles = dict()
            for key, value in letters.items():
                if value >= k:
                    possibles[key] = math.floor(value/k)
            iter = list(possibles.keys())
            iter.sort()
            res = ""
            q = deque([""])
            while q:
                curr = q.popleft()
                for ch in iter:
                    nxt = curr + ch
                    if isK(nxt, s, k):
                        res = nxt
                        q.append(nxt)
            return res
                
            
            
Solution().longestSubsequenceRepeatedK("gbjbjigjbji",2)
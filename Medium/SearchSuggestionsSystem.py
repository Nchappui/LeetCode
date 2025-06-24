from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        matching = []
        def traverse(prefix, curr):
            if not curr or len(matching)== 3:
                return
            if '*' in curr:
                matching.append(prefix)
            for elem in curr:
                traverse(prefix + elem, curr[elem])
                
        products.sort()
        root = dict()
        for product in products:
            curr = root
            for c in product:
                if c not in curr:
                    curr[c] = dict()
                curr = curr[c]
            curr['*'] = None
        
        prefix = ""
        res = []
        notFound = False
        for letter in searchWord:
            matching = []
            prefix += letter
            if letter in root and not notFound:
                root = root[letter]
                traverse(prefix, root)
            else:
                notFound = True
            res.append(matching) 
        
        return(res)
        
Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse")
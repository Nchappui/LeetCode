from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def checkPair (newPair):
            oldpairs = pairs.copy()
            for j in range(len(newPair)):
                    for pair in oldpairs:
                        if newPair[j] in pair and newPair[j-1] not in pair:
                            newLetter = pair[pair.index(newPair[j])-1]
                            commonLetter = newPair[j]
                            otherLetter = newPair[j-1]
                            if ((newLetter, otherLetter) not in equationDict):
                                equationDict[newLetter, otherLetter] = equationDict[newLetter, commonLetter] * equationDict[commonLetter, otherLetter]
                                equationDict[otherLetter, newLetter] = 1 / equationDict[newLetter, otherLetter]
                                pairs.append([newLetter, otherLetter])
                                checkPair([newLetter, otherLetter])
        equationDict = {}
        pairs= []
        letters = set()
        for i in range(len(equations)):
            letters.add(equations[i][0])
            letters.add(equations[i][1])
            if (equations[i][0],equations[i][1]) not in equationDict:
                equationDict[(equations[i][0],equations[i][1])] = values[i]
                equationDict[equations[i][1],equations[i][0]] = 1/values[i]            
                pairs.append([equations[i][0],equations[i][1]])
                checkPair((equations[i][0],equations[i][1]))
        
        res = []
        for query in queries:
            res.append(equationDict.get((query[0],query[1]), -1))
            if query[0] == query[1] and query[0] in letters:
                res[-1] = 1
        return res
    ### Rien compris mdr
    def calcEquation2(self, equations, values, queries):
        g={}
        for (a,b),v in zip(equations,values):
            g.setdefault(a,{})[b]=v
            g.setdefault(b,{})[a]=1.0/v
        def f(x,y):
            if x not in g or y not in g:
                return -1.0
            s=[(x,1.0)]
            v=set()
            while s:
                c,r=s.pop()
                if c==y:
                    return r
                v.add(c)
                for n in g[c]:
                    if n not in v:
                        s.append((n,r*g[c][n]))
            return -1.0
        return [f(a,b) for a,b in queries]


            

print(Solution().calcEquation([["a","b"],["e","f"],["b","e"]],[3.4,1.4,2.3],[["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]))


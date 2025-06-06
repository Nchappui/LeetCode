from collections import defaultdict

class Solution:
    ## NOT WORKING I SPENT TOO MUCH TIME
    def smallestEquivalentString2(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        equivMap = dict()
        revEquivMap = dict()
        res = ""
        for i in range(n):
            c1, c2 = s1[i], s2[i]
            if c1 < c2:
                if c2 in equivMap.keys():
                    if c1 < equivMap[c2]:
                        temp = revEquivMap.pop(equivMap[c2])
                        temp.append(equivMap[c2])
                        revEquivMap[c1] = temp
                        for elem in revEquivMap[c1]:
                            equivMap[elem] = c1
                            
                else:
                    if c1 in equivMap.keys():
                        equivMap[c2] = equivMap[c1]
                        revEquivMap[equivMap[c1]].append(c2)
                    else:
                        equivMap[c2] = c1
                        if c1 in revEquivMap.keys():
                            revEquivMap[c1].append(c2)
                        else:
                            revEquivMap[c1] = [c2]
            elif c2 < c1:
                if c1 in equivMap.keys():
                    if c2 < equivMap[c1]:
                        temp = revEquivMap.pop(equivMap[c1])
                        temp.append(equivMap[c1])
                        revEquivMap[c2] = temp
                        for elem in revEquivMap[c2]:
                            equivMap[elem] = c2
                else:
                    if c2 in equivMap.keys():
                        equivMap[c1] = equivMap[c2]
                        revEquivMap[equivMap[c2]].append(c1)
                    else:
                        equivMap[c1] = c2
                        if c2 in revEquivMap.keys():
                            revEquivMap[c2].append(c1)
                        else:
                            revEquivMap[c2] = [c1]

        charToChange = equivMap.keys()
        for i in range(len(baseStr)):
            if baseStr[i] in charToChange:
                res += equivMap[baseStr[i]]
            else:
                res += baseStr[i]
        return res
    
    def smallestEquivalentString(self, s1, s2, baseStr):
        adj = defaultdict(list)

        # Step 1: Build the graph
        for a, b in zip(s1, s2):
            adj[a].append(b)
            adj[b].append(a)

        def dfs(ch, visited):
            visited.add(ch)
            min_ch = ch
            for nei in adj[ch]:
                if nei not in visited:
                    candidate = dfs(nei, visited)
                    min_ch = min(min_ch, candidate)
            return min_ch

        result = []
        for ch in baseStr:
            visited = set()
            result.append(dfs(ch, visited))
        
        return ''.join(result)
    

print(Solution().smallestEquivalentString("bcfeaabddgcdaefcbfadggfagfgfedeefbebdbeefbecggcgge", "feegaacabcfadggfcaabcbadbbecbfdcabgeaegfcagdfggdgg", "mytnpodxbwxcxcplapgrqjzkfrkizffkbquwqbkxmpqjmxykvb"))
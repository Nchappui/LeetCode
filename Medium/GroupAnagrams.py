from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        stringsMap = {}
        for elem in strs:
            sortedString = "".join(sorted(elem)) 
            if sortedString in stringsMap.keys():
                res[stringsMap[sortedString]].append(elem)
            else:
                stringsMap[sortedString] = len(res)
                res.append([elem])

        return res
    
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
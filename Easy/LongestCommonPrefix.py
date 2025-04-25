from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        currentPrefix=""
        while len(currentPrefix)<len(strs[0]):
            currentPrefix=strs[0][0:len(currentPrefix)+1]
            for elem in strs[1:]:
                if(elem[:len(currentPrefix):]!=currentPrefix):
                    return currentPrefix[:-1]

        return currentPrefix

print(Solution().longestCommonPrefix(["flower"])) 

print(Solution().longestCommonPrefix(["flower","flow","flight"])) 

print(Solution().longestCommonPrefix(["dog","racecar","car"])) 


from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = chars[0]
        num = 1
        index = 1
        for elem in chars[1:]:
            if elem == prev:
                num += 1
                chars.pop(index)
            else:
                if num != 1:
                    strnum = str(num)
                    for i in range(len(strnum)):
                        chars.insert(index,strnum[i])
                        index += 1
                index += 1
                prev = elem
                num = 1

        if num >1:
            strnum = str(num)
            for i in range(len(strnum)):
                chars.append(strnum[i])
        return len(chars)
    
Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b","a","b","b","b","b","b","b","b","b","b","b","b","b"])
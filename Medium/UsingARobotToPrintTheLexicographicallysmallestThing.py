import heapq

class Solution:
    def robotWithString(self, s: str) -> str:
        t = ""
        res = ""
        sheap = []
        previndex = -1
        calcIndex = 0
        removedFromS = True
        smin = 'x'
        index = 0
        for i in range(len(s)):
            heapq.heappush(sheap, (s[i],i))
        while s or t:
            
            if not s:
                res += t[::-1]
                return res
            
            if removedFromS:
                smin, index = heapq.heappop(sheap)
                while previndex > index:
                    smin, index = heapq.heappop(sheap)
                removedFromS = False

            previndex = index

            calcIndex = index - len(res) - len(t)
            if not t:
                t = s[0:calcIndex]
                res += s[calcIndex]
                s = s[calcIndex+1:]
                removedFromS = True
            else:
                if t[-1] <= smin:
                    res += t[-1]
                    t = t[:-1]
                else:
                    t += s[0:calcIndex]
                    res += s[calcIndex]
                    s = s[calcIndex+1:]
                    removedFromS = True

        return res
    

print(Solution().robotWithString("EDDADDDA"))
print(Solution().robotWithString("EDDADDD"))
print(Solution().robotWithString("CDDADDD"))
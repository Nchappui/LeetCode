from collections import defaultdict
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        ans = float('-inf')

        ## a must be odd and maximal
        ## b must be even and minimal
        maxDiff = -1
        for a in ["0","1","2","3","4"]:
            for b in ["0","1","2","3","4"]:
                if a == b:
                    continue
                s1 = [0]
                s2 = [0]
                for i in range(len(s)):
                    if s[i] == a:
                        s1.append(s1[-1]+1)
                        s2.append(s2[-1])
                    elif s[i] == b:
                        s1.append(s1[-1])
                        s2.append(s2[-1]+1)
                    else:
                        s1.append(s1[-1])
                        s2.append(s2[-1])
                if s1[-1] < 1 or s2[-1] < 2:
                    continue

                g = [[float('-inf')] * 2 for _ in range(2)]
                start = 0    

                # Step 4: Two-pointer sliding window
                for end in range(k, n + 1):
                    while end - start >= k and s1[end] > s1[start] and s2[end] > s2[start]:
                        pa = s1[start] % 2
                        pb = s2[start] % 2
                        g[pa][pb] = max(g[pa][pb], s2[start] - s1[start])
                        start += 1

                    # Step 5: Check candidate answer
                    pa = s1[end] % 2
                    pb = s2[end] % 2
                    best = g[1 - pa][pb]
                    if best != float('-inf'):
                        ans = max(ans, (s1[end] - s2[end]) + best)

        return -1 if ans == float('-inf') else ans # type: ignore

    
print(Solution().maxDifference("12233",4))
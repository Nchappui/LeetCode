class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if k>n : return 0
        elif k == n : return 1
        count = 1
        groups = []
        totalStrings = 1
        for i in range(1,n):
            if word[i] == word[i-1]:
                count += 1
            else:
                groups.append(count)
                totalStrings *= count
                count = 1
        groups.append(count)
        mod = 10**9 + 7
        totalStrings = (totalStrings * count) % mod
        nbGroups = len(groups)
        if k <= nbGroups: return totalStrings
        
        dp = [0] * k
        dp[0] = 1
        
        for num in groups:
            newDp = [0] * k
            sum_val = 0
            for i in range(k):
                if i > 0 : 
                    sum_val = (sum_val + dp[i-1]) % mod
                if i > num:
                    sum_val = (sum_val - dp[i - num - 1] + mod) % mod
                newDp[i] = sum_val
            dp = newDp
        invalid = sum(dp[len(groups):k]) % mod
        return (totalStrings - invalid + mod) % mod
        
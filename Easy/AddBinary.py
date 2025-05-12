class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = len(a) if len(a) > len (b) else len(b)
        r = False
        res = ""
        a = a[::-1]
        b = b[::-1]
        for i in range(n):
            x = a[i] if i < len(a) else '0'
            y = b[i] if i < len(b) else '0'
            if x != y:
                res = '0' + res if r else '1' + res
            else:
                res = '1' + res if r else '0' + res
                r = True if x == "1" else False
        if r :
            res = '1' + res
        return res
    
print(Solution().addBinary("1010","1011"))
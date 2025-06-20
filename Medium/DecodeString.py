class Solution:
    def decodeString(self, s: str) -> str:
        temp = ""
        res = ""
        letterStack = []
        multStack = []
        brackCount = 0
        for i in range(len(s)):
            if s[i] in "0123456789":
                if len(multStack) == brackCount:
                    multStack.append("")
                multStack[brackCount] += s[i]
            elif s[i] == "[":
                brackCount += 1
                letterStack.append("")
            elif s[i] == "]":
                brackCount -= 1
                mult = int(multStack.pop())
                letters = letterStack.pop()
                while mult:
                    temp += letters
                    mult -= 1
                if brackCount:
                    letterStack[-1] += temp
                else:
                    res += temp
                temp = ""
            else:
                if not brackCount:
                    res += s[i]
                else:
                    letterStack[brackCount-1] += s[i]
        return res

print(Solution().decodeString("100[leetcode]"))
print(Solution().decodeString("3[a2[c4[d]]]"))
print(Solution().decodeString("aa3[2[b]3[c]]zz"))

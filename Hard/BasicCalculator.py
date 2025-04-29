class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == " ":
                continue
            if s[i] == ")":
                temp = 0
                while stack[len(stack)-2] != "(" and stack[len(stack)-1] != "(":
                    number = stack.pop()
                    temp += int(stack.pop() + number)
                if stack[len(stack)-2] == "(":
                    number = stack.pop()
                    stack.pop()
                    temp += int(number)
                else:
                    stack.pop()
                stack.append(str(temp))
            else:
                stack.append(s[i])
        temp = 0
        while len(stack) > 1:
            number = stack.pop()
            temp += int(stack.pop() + number)

        return int(stack[0]) + temp if len(stack) > 0 else temp
    
print(Solution().calculate("1 + 1")) ##2
print(Solution().calculate(" 2-1 + 2 ")) ## 3
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)")) ##23
print(Solution().calculate("(1-(4+5+2)-3)+(6+8)")) ##1
print(Solution().calculate("-(1+(4+5+2)-3)+(6+8)")) ##-23

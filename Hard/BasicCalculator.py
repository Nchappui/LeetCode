class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        currentNumber = float('inf')
        for i in range(len(s)):
            if s[i] == " ":
                continue
            if s[i] == ")":
                if currentNumber!=float('inf'):
                    stack.append(str(currentNumber))
                currentNumber=float('inf')
                temp = 0
                while stack[len(stack)-2] != "(" and stack[len(stack)-1] != "(":
                    number = stack.pop()
                    sign = stack.pop()
                    if sign == "-" and int(number)<0:
                        temp += int(number[1:])
                    elif sign == "+" and int(number)<0:
                        temp -= int(number[1:])
                    else:
                        temp += int(sign + number)
                if stack[len(stack)-2] == "(":
                    number = stack.pop()
                    stack.pop()
                    temp += int(number)
                else:
                    stack.pop()
                stack.append(str(temp))
            elif s[i] == "+" or s[i] == "-" or s[i] == "(":
                if currentNumber!=float('inf'):
                    stack.append(str(currentNumber))
                    currentNumber=float('inf')
                stack.append(s[i])
            else:
                if currentNumber!=float('inf'):
                    currentNumber = currentNumber * 10 + int(s[i])
                else:
                    currentNumber = int(s[i])
        if(currentNumber!=float('inf')):
            stack.append(str(currentNumber))
        temp = 0
        while len(stack) > 1:
            number = stack.pop()
            sign = stack.pop()
            if sign == "-" and int(number)<0:
                temp += int(number[1:])
            elif sign == "+" and int(number)<0:
                temp -= int(number[1:])
            else:
                temp += int(sign + number)

        return int(stack[0]) + temp if len(stack) > 0 else temp

    def calculate2(self, s: str) -> int:
        def update(op, v):
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
            if op == "*": stack.append(stack.pop() * v)           #for BC II and BC III
            if op == "/": stack.append(int(stack.pop() / v))      #for BC II and BC III
    
        it, num, stack, sign = 0, 0, [], "+"
        
        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] in "+-*/":
                update(sign, num)
                num, sign = 0, s[it]
            elif s[it] == "(":                                        # For BC I and BC III
                num, j = self.calculate2(s[it + 1:])
                it = it + j
            elif s[it] == ")":                                        # For BC I and BC III
                update(sign, num)
                return sum(stack), it + 1
            it += 1
        update(sign, num)
        return sum(stack)

print(Solution().calculate("5+3-4-(1+2-7+(10-1+3+5+(3-0+(8-(3+(8-(10-(6-10-8-7+(0+0+7)-10+5-3-2+(9+0+(7+(2-(2-(9)-2+5+4+2+(2+9+1+5+5-8-9-2-9+1+0)-(5-(9)-(0-(7+9)+(10+(6-4+6))+0-2+(10+7+(8+(7-(8-(3)+(2)+(10-6+10-(2)-7-(2)+(3+(8))+(1-3-8)+6-(4+1)+(6))+6-(1)-(10+(4)+(8)+(5+(0))+(3-(6))-(9)-(4)+(2))))))-1)))+(9+6)+(0))))+3-(1))+(7))))))))"))##-35
print(Solution().calculate("1-(2+3-(4+(5-(1-(2+4-(5+6))))))"))##-1
print(Solution().calculate("(1-(3-4))"))##2
print(Solution().calculate("-(1-(3-4))"))##-2     
print(Solution().calculate("1-(      -1)"))##2
print(Solution().calculate("1-(      -2)"))##3
print(Solution().calculate("1 + 1")) ##2
print(Solution().calculate(" 2-1 + 2 ")) ## 3
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)")) ##23
print(Solution().calculate("2147483647")) ##2147483647
print(Solution().calculate("(1-(4+5+20)-3)+(6+8)+10")) ##-7
print(Solution().calculate("-(1+(4+5+2)-3)+(6+8)")) ##5
print(Solution().calculate("-((1+(4+5+2)-3)+(6+8))")) ##-23

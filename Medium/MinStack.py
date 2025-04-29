class MinStack:
    def __init__(self):
        self.stack = []
        self.current_min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append([val, self.current_min])
        self.current_min = min(self.current_min, val)

    def pop(self) -> None:
        if self.stack[len(self.stack)-1][0] == self.current_min:
            self.current_min = self.stack[len(self.stack)-1][1]
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1][0]
        

    def getMin(self) -> int:
        return self.current_min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
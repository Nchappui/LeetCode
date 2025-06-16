class RecentCounter:

    def __init__(self):
        self.stack = []

    def ping(self, t: int) -> int:
        self.stack.append(t)
        n = len(self.stack)
        i= 0
        while (i < n and self.stack[n-i-1] >= t-3000):
            i+=1
        return i
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
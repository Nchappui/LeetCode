class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price,1))
            return 1
        else:
            if self.stack[-1][0] > price:
                self.stack.append((price,1))
                return 1
            else:
                i = 0
                n = len(self.stack)
                while(i < n and self.stack[-1 - i][0] <= price):
                    i += self.stack[-1 - i][1]
                self.stack.append((price, i+1))
                return i + 1


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(100)
param_2 = obj.next(80)
param_3 = obj.next(60)
param_4 = obj.next(70)
param_5 = obj.next(60)
param_6 = obj.next(75)
param_7 = obj.next(85)
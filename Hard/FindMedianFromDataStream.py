import heapq

class MedianFinder:

    def __init__(self):
        self.n = 0
        self.lower = []
        self.upper = []
        self.median = None
        

    def addNum(self, num: int) -> None:
        if self.n == 0:
            self.median = num         
        else:
            if self.n%2:
                if num < self.median:
                    heapq.heappush(self.lower, -num)
                    heapq.heappush(self.upper, self.median)
                else:
                    heapq.heappush(self.lower, -self.median)
                    heapq.heappush(self.upper, num)
                self.median = (-self.lower[0] + self.upper[0])/2
            else:
                if num < -self.lower[0]:
                    self.median = -heapq.heappop(self.lower)
                    heapq.heappush(self.lower, -num)
                elif num >self.upper[0]:
                    self.median = heapq.heappop(self.upper)
                    heapq.heappush(self.upper, num)
                else:
                    self.median = num
        self.n += 1

    def findMedian(self) -> float:
        return self.median



# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(3)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(5)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(0)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(2)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(4)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(6)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(7)
param_2 = obj.findMedian()
print(param_2)
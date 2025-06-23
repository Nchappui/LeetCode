import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.heap = []

    def popSmallest(self) -> int:
        if not self.heap:
            self.smallest += 1
            return self.smallest - 1
        else:
            return heapq.heappop(self.heap)

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.heap:
            heapq.heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
obj.addBack(2)
print(obj.popSmallest())

print(obj.popSmallest())

print(obj.popSmallest())

obj.addBack(1)

print(obj.popSmallest())

print(obj.popSmallest())

print(obj.popSmallest())

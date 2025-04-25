import random

class RandomizedSet:
    hashMap = {}
    def __init__(self):
        self.hashMap = {}

    def insert(self, val: int) -> bool:
        if self.hashMap.get(val, True):
            self.hashMap.update({val :val})
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            self.hashMap.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.hashMap.get(random.choice(list(self.hashMap.keys)))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
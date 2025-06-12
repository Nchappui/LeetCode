from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 1 and n>0 or flowerbed[0] == 0 and n>1:
                return False
            else: 
                return True

        if n<=0:
            return True
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0]=1
            n-=1

        for i in range(1, len(flowerbed)-1):
            if n<=0:
                return True
            if not flowerbed[i-1] and not flowerbed[i] and not flowerbed[i+1]:
                flowerbed[i] = 1
                n-=1
        
        if not flowerbed[-1] and not flowerbed[-2]:
            flowerbed[-1]=1
            n-=1

        if n<=0:
            return True
        
        return False